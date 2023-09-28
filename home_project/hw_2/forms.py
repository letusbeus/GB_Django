from django import forms


class ProductAddForm(forms.Form):
    product_title = forms.CharField(max_length=100, required=True, label='Product', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter product title'}))
    product_description = forms.CharField(label='Description',
                                          widget=forms.Textarea(attrs={'placeholder': 'Describe the product'}))
    product_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price:')
    product_quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_image = forms.ImageField(label='Product image')
