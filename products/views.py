from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .forms import ProductForm
from .models import Product

# Create your views here.

# /products/


def index(request):
    products = Product.objects.all()

    return render(
        request,
        'index.html',
        context={'products': products}
    )


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'detail.html',
        context={'product': product})


def form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()

    return render(
        request,
        'product_form.html',
        {'form': form}
    )
