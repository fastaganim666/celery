from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category, SubscribersCategory


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['name', 'text', 'categories', 'type']

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            text = cleaned_data.get("text")
            if name == text:
                raise ValidationError(
                   "Описание не должно быть идентично названию."
                )
            return cleaned_data
        


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribersCategory
        fields = ['category', ]


