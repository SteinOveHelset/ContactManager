from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect

from contact.models import Contact

@login_required
def frontpage(request):
    contacts = Contact.objects.filter(created_by=request.user)

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {
        'form': form
    })