from django.shortcuts import (HttpResponsePermanentRedirect,
                              HttpResponseRedirect, redirect, render)
from item.models import Category, Item, Value

from .forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'porto/index.html', {
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request, 'porto/contact.html')

def base(request):
    return render(request , 'porto/base.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'porto/signup.html', {
        'form': form
    })