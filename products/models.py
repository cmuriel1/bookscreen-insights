from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    class PRODUCT_TYPE(models.TextChoices):
        MOVIE = 'movies', 'Movie'
        BOOK = 'books', 'Book'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE.choices)
    title = models.CharField(max_length=220)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_average_rating(self):
        all_reviews = self.comment_set.all()
        all_rating = 0

        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += int(review.rating)
            
            return round(all_rating / len(all_reviews), 2)
        return '-'

    def count_rating(self):
        all_reviews = self.comment_set.all()
        count = all_reviews.count()
        return count


def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == '':
        new_slug = slugify(instance.title)
        klass = instance.__class__
        qs = klass.objects.filter(
            slug__icontains=new_slug).exclude(id=instance.id)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f'{new_slug}-{qs.count()}'


pre_save.connect(slugify_pre_save, sender=Category)
pre_save.connect(slugify_pre_save, sender=Product)