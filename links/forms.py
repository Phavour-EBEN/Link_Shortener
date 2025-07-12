from django import forms
from .models import Link


class Link_form(forms.ModelForm):
    # original_url = forms.URLField(max_length=200, required=True, label="Original URL")
    # short_url = forms.CharField(max_length=50, required=True, label="Short URL")
    # slug = forms.SlugField(max_length=50, required=False, label="Slug")
    class Meta:
        model = Link
        fields = ['original_url', 'short_url', 'slug']