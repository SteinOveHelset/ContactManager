from django.shortcuts import get_object_or_404, render, redirect

from .models import Category, Contact

def add(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')

        Contact.objects.create(
            category_id=category_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            zipcode=zipcode,
            city=city,
        )

        return redirect('frontpage')

    categories = Category.objects.all()

    return render(request, 'contact/add.html', {
        'categories': categories
    })

def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        contact.category_id = request.POST.get('category')
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.address = request.POST.get('address')
        contact.zipcode = request.POST.get('zipcode')
        contact.city = request.POST.get('city')
        contact.save()

        return redirect('frontpage')

    return render(request, 'contact/edit.html', {
        'contact': contact,
        'categories': categories
    })

def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()

    return redirect('frontpage')