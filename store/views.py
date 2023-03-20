from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def diagrams(request):
    c1_no = Product.objects.filter(category_id='1').count()
    c1_no = int(c1_no)
    print('Number of parfumeriya products:',c1_no)

    c3_no = Product.objects.filter(category_id='3').count()
    c3_no = int(c3_no)
    print('Number of oblichchya products:',c3_no)
    
    c4_no = Product.objects.filter(category_id='4').count()
    c4_no = int(c4_no)
    print('Number of volossya products:',c4_no)

    c5_no = Product.objects.filter(category_id='5').count()
    c5_no = int(c5_no)
    print('Number of makiyazh products:',c5_no)

    c6_no = Product.objects.filter(category_id='6').count()
    c6_no = int(c6_no)
    print('Number of makiyazh products:',c6_no)

    france_no = Product.objects.filter(brand='Франція').count()
    france_no = int(france_no)
    print('Number of French products:',france_no)

    canada_no = Product.objects.filter(brand='Канада').count()
    canada_no = int(canada_no)
    print('Number of Canadian products:',canada_no)

    usa_no = Product.objects.filter(brand='США').count()
    usa_no = int(usa_no)
    print('Number of USA products:',usa_no)

    brand_list = ['Франція', 'Канада', 'США']
    brand_number = [france_no, canada_no, usa_no]

    productsCatgId_list = ['Парфумерія', 'Обличчя', 'Волосся', 'Макіяж', 'Тіло і ванна']
    number_list = [c1_no, c3_no, c4_no, c5_no, c6_no]
    context = {'productsCatgId_list':productsCatgId_list, 'number_list':number_list, 'brand_list':brand_list, 'brand_number':brand_number}
    return render(request, 'store/diagrams.html', context)