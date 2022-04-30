from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders

def index(request):
    products = Product.objects.all()
    #pid = Product.objects.get(product_name='Reebook')
    #print(pid.id)
    #allProducts = [[products,range(1,len(products))],[products,range(1,len(products))]]   'testing'
    #params = {'product':products,range:range(len(products))}
    allProducts = []
    categoryProducts = Product.objects.values('subCategory')
    categoryProduct = {item['subCategory'] for item in categoryProducts }
    for categ in categoryProduct:
        product = Product.objects.filter(subCategory=categ)
        allProducts.append([product,range(len(products))])
    params = {'allProducts':allProducts}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phoneno','')
        desc =  request.POST.get('desc','')
        #print(name,email,phone,desc)
        contacts = Contact( contact_name=name, contact_email=email, contact_phone=phone, contact_desc=desc)
        contacts.save()
    return render(request,'shop/contact.html')

def searchMatch(query,item):
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    products = Product.objects.all()
    allProducts = []
    categoryProducts = Product.objects.values('category')
    categoryProduct = {item['category'] for item in categoryProducts }
    for categ in categoryProduct:
        productemp = Product.objects.filter(category=categ)
        product = [item for item in productemp if searchMatch(query,item)]
        if len(product)!= 0:
            allProducts.append([product,range(len(products))])
    params = {'allProducts':allProducts,'msg':''}
    if len(allProducts) == 0:
        params = {'msg':'Search Result Not Found...'}
        return render(request,'shop/search.html',params)
    else:
        return render(request,'shop/index.html',params)

def tracker(request):
    return render(request,'shop/tracker.html')


def productView(request,id):
    singleproduct = Product.objects.filter(id=id)
    print(singleproduct)
    return render(request,'shop/productView.html',{'product':singleproduct[0]})


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        address2 = request.POST.get('address2','')
        phone = request.POST.get('phone','')
        city =  request.POST.get('city','')
        state =  request.POST.get('state','')
        zip =  request.POST.get('zip','')
        #print(name,email,phone)
        orders = Orders(name=name,email=email,address=address,address2=address2,phone=phone,city=city,state=state,zip=zip)
        orders.save()
    return render(request,'shop/checkout.html')
