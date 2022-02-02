from django import forms
from .models import Menu, Category, SubCategory


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_name = [(s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names
        self.fields['subcategory'].choices = friendly_name