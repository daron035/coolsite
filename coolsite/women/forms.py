from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat'] #'__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    
    def clean_title(self): # валидация поля title, которую мы прописываем сами
        title = self.cleaned_data['title'] # если не прописывать валидаторы, они будут проверяться в классе модели
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        
        return title # также можно прописать валидатор для любого другого поля