from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('category', 'first_name', 'last_name', 'email', 'phone', 'address', 'zipcode', 'city')