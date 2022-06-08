from django.db.models import Q
from django.shortcuts import render

from contact.models import Contact

def frontpage(request):
    contacts = Contact.objects.all()

    query = request.GET.get('query', '')

    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            |
            Q(last_name__icontains=query)
            |
            Q(email__icontains=query)
            |
            Q(phone__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(zipcode__icontains=query)
            |
            Q(city__icontains=query)
        )

    return render(request, 'core/frontpage.html', {
        'contacts': contacts
    })