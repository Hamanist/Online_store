from django import forms

from catalog.models import Product, ProductVersion


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Запрещенные слова ' + word)
        return cleaned_data

    def clean_description(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Запрещенные слова ' + word)
        return cleaned_data


class ProductVersionForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = '__all__'
