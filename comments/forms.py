from django import forms 

from .models import Comment


INPUT_STYLE = "mb-3 bg-gray-50 mb-7 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

RATING_STYLE = "mb-5 mt-2 bg-gray-50 mb-7 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

# Write a comment...

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user',
            'product',
            'comment',
            'rating'
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs['class'] = INPUT_STYLE
        self.fields['comment'].widget.attrs['placeholder'] = 'Write a comment...'

        self.fields['rating'].widget.attrs['class'] = RATING_STYLE