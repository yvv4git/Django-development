# -*- coding: utf-8 -*-
from django import forms            # импортируем формы
from .models import Post            # импортируем нашу модель

class PostForm(forms.ModelForm):
    class Meta:
        model = Post                    # какая модель будет использоваться для созадания формы
        fields = ('title', 'text',)     # какие поля будут у формы
