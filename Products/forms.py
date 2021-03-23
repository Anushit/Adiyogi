from django import forms
from .models import Category,Product

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','slug','status']

class UpdateCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug','description']



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug','price']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug','price']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price','image','status']

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['title','price','image','status']

