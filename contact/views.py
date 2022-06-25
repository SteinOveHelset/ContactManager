from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .forms import ContactForm
from .models import Category, Contact

@login_required
def add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user
            contact.save()
        
            return redirect('frontpage')

    categories = Category.objects.all()

    return render(request, 'contact/add.html', {
        'categories': categories
    })

@login_required
def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk, created_by=request.user)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()

            return redirect('frontpage')
    else:
        form = ContactForm()

    return render(request, 'contact/edit.html', {
        'contact': contact,
        'categories': categories
    })

@login_required
def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, created_by=request.user)
    contact.delete()

    return redirect('frontpage')