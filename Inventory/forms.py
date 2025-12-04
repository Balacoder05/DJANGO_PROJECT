from django .forms import ModelForm
from .models import*

class Product_Form(ModelForm):

    class Meta:
        model=Product
        fields='__all__'
        # fields=['Product_name','Price'] for speacial fields only

    