from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Запрещенные слова' + word)
        return cleaned_data

    def clean_description(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Запрещенные слова' + word)
        return cleaned_data
