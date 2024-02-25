from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Category, Product
from comments.forms import CommentForm


def home(request):
    context = {}
    return render(request, 'home.html', context)


def search(request):
    categoires = Category.objects.all()
    products = Product.objects.all()
    products_count = products.count()

    page_title = 'Moives and Books'
    context = {
        'categoires': categoires,
        'products': products,
        'products_count': products_count,
        'page_title': page_title
    }
    return render(request, 'products/search.html', context)


def product_details(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    comments = product.comment_set.all()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.product = product
        new_comment.save()
        return redirect(f"/product/{product.slug}")

    print(product.get_average_rating())

    context = {
        'product': product,
        'form': form,
        'comments': comments,
    }
    return render(request, 'products/details.html', context)


def product_search_categories(request, slug=None):
    products = Product.objects.filter(
        Q(product_type=slug) | Q(category__title=slug)
    )

    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    products_count = products.count()

    categoires = Category.objects.all()
    page_title = slug
    context = {
        'categoires': categoires,
        'products': products,
        'products_count': products_count,
        'page_title': page_title
    }
    return render(request, 'products/search.html', context)
