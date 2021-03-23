from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product
from .forms import AddCategoryForm,UpdateCatForm,AddProductForm,UpdateProductForm,AddItemForm,UpdateItemForm
from math import ceil
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ItemSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def AllProducts(request):
    products = Product.objects.all().filter(status=True)

    context = {
        'products': products,

    }
    return render(request, 'frontend/home1.html', context)

def Items(request):
    #items = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
    return render(request, 'frontend/home.html', params)
    #context = {
       # 'items': items
   # }
    #return render(request, 'frontend/home.html', context)

def SearchResultsView(request):
        if request.method == "GET":
            search = request.GET.get('search')
            products = Product.objects.all().filter(title__icontains=search)
            return render(request, 'frontend/search.html', {'products': products})
def categorytable(request):
    cats = Category.objects.all()

    context = {
        'cats': cats,
    }
    return render(request, 'backend/categorytable.html', context)



def AddCategory(request):
    cats = Category.objects.all()
    if request.method == 'POST':
        fm = AddCategoryForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            slug = fm.cleaned_data['slug']
            status = fm.cleaned_data['status']
            Add = Category(title=title, slug=slug,status=status)
            Add.save()
            return redirect('categorytable')
    else:
        fm = AddCategoryForm()
    return render(request,'backend/addcategory.html',{'form':fm, 'cats':cats})


def delete_Category(request,id):
    if request.method == "POST":
        pi=Category.objects.get(pk=id)
        pi.delete()
        return redirect('categorytable')

def Update_Category(request,id):
    if request.method == "POST":
        pi = Category.objects.get(pk=id)
        fm = UpdateCatForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('categorytable')
    else:
         pi = Category.objects.get(pk=id)
         fm = UpdateCatForm(instance=pi)
    return render(request,'backend/updatecat.html',{'form':fm, 'pi':pi})



def ProductTable(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'backend/producttable.html', context)

def AddProduct(request):
    catprod = Category.objects.all()
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            price = request.POST['price']
            slug = request.POST['slug']
            category = request.POST['category']
            category = get_object_or_404(Category, pk=category)
            prod = Product(title=title,price=price,slug=slug,category_id=category.id)
            prod.save()
            return redirect('ProductTable')
        else:
            form = AddProductForm(request.POST)
            return render(request, 'backend/AddProduct.html', {'form': form, 'catprod': catprod})

    else:
        form = AddProductForm()
        return render(request, 'backend/AddProduct.html', {'form': form, 'catprod': catprod})

def delete_Product(request,id):
    if request.method == "POST":
        pi=Product.objects.get(pk=id)
        pi.delete()
        return redirect('ProductTable')


def Update_Product(request,id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = UpdateProductForm(request.POST, instance=pi)
        print(fm)
        if fm.is_valid():
            fm.save()
            return redirect('ProductTable')
    else:
         pi = Product.objects.get(pk=id)
         fm = UpdateProductForm(instance=pi)
    return render(request,'backend/UpdateProduct.html',{'form':fm, 'pi':pi})

def AddItem(request):
        Items = Category.objects.all()
        if request.method == "POST":
            form = AddItemForm(request.POST, request.FILES)
            if form.is_valid():
                title = request.POST['title']
                price = request.POST['price']
                image = request.FILES['image']
                category = request.POST['category']
                category = get_object_or_404(Category, pk=category)
                prod = Product(title=title, price=price, image=image,category_id=category.id)
                prod.save()
                return redirect('ItemTable')
            else:
                form = AddItemForm(request.POST)
                return render(request, 'backend/AddItem.html', {'form': form, 'Items': Items})

        else:
            form = AddItemForm()
            return render(request, 'backend/AddItem.html', {'form': form, 'Items': Items})


def ItemStatus(request,id):
    products = Product.objects.get(id=id)
    if products.status:
        products.status = False
    else:
        products.status = True
    products.save()
    products = Product.objects.all()
    return render(request, 'backend/ItemTable.html', {'products': products})


def ItemTable(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'backend/ItemTable.html', context)


def delete_Item(request,id):
    if request.method == "POST":
        pi=Product.objects.get(pk=id)
        pi.delete()
        return redirect('ItemTable')

def Update_Item(request,id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = UpdateItemForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('ItemTable')
    else:
         pi = Product.objects.get(pk=id)
         fm = UpdateItemForm(request.FILES,instance=pi)
    return render(request,'backend/UpdateItem.html',{'form':fm, 'pi':pi})

def shop(request):
    products = Product.objects.all().filter(status=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories':categories,
    }
    return render(request,'frontend/Product.html',context)

def SearchResultsView(request):
        if request.method == "GET":
            search = request.GET.get('search')
            products = Product.objects.all().filter(title__icontains=search)
            return render(request, 'frontend/search.html', {'products': products})


def product_detail(request,id):
    category = Category.objects.all()
    product = Product.objects.filter(pk=id)
    context = {
        'category':category,
        'product':product,
    }
    return render(request, 'frontend/product_detail.html',context)

@csrf_exempt
def details_view(request,id):
    try:
        products = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(products)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ItemSerializer(products, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)

