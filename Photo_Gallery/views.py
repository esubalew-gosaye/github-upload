from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
import requests
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *


def gallery(request):
    category_name = request.GET.get('category', 'All')
    if category_name == 'All':
        gallery = Gallery.objects.all()
    elif category_name == 'none':
        gallery = Gallery.objects.filter(category_id=None)
    else:
        category = Category.objects.get(name=category_name)
        gallery = category.gallery_set.all()
    # category Paginator
    category = Category.objects.all().order_by('name')
    pag = Paginator(category, 3)
    nums = request.GET.get('cpage', '1')
    category = pag.get_page(nums)
    # Gallery Paginator
    gpag = Paginator(gallery.order_by('category__name'), 6)
    gallery = gpag.get_page(request.GET.get('gpage', '1'))
    gpages = gpag.num_pages
    context = {'photos': gallery, 'categories': category, 'pages': pag.num_pages, 'gpages': gpages}
    return render(request, 'photo_gallery/gallery.html', context)


def viewphoto(request, pk):
    photo = Gallery.objects.get(id=pk)
    return render(request, 'photo_gallery/photo.html', {'photo': photo})


def add(request):
    category = Category.objects.all()
    if request.method == "POST":
        photo = request.FILES.get('images')
        data = request.POST
        category = None
        created = None
        if data['category'] != 'none':
            category = Category.objects.get(name=data['category'])
        else:
            if category != '':
                category, created = Category.objects.get_or_create(name=data['category_new'].title())

        Gallery.objects.create(
            description=data['description'],
            category=category,
            photo=photo
        )
        return redirect('gallery')
    context = {'photos': '', 'categories': category}
    return render(request, 'photo_gallery/add.html', context)


def register(request):
    if request.method == 'POST':
        nam = request.POST.get('name', False)
        email = request.POST['email']
        password = request.POST['password']
        if nam:
            name = request.POST['name']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User already registered, Please login')
                return redirect('register')
            else:
                user = User(name=name, email=email, password=password)
                user.save()
                messages.success(request, 'Welcome, ' + name + '!')
                return redirect('gallery')
        else:
            if User.objects.filter(email=email, password=password).exists():
                user_info = User.objects.get(email=email)
                if user_info.admin:
                    messages.success(request, 'Welcome, ' + user_info.name + '!')
                    return redirect('admin_portal')
                else:
                    messages.success(request, 'Welcome, ' + user_info.name + '!')
                    return redirect('gallery')
            else:
                messages.error(request, 'No User with this credentials')
                return redirect('register')

    return render(request, 'photo_gallery/login_register.html')


def admin_portal(request):
    return render(request, 'photo_gallery/admin_portal.html')


# def pie(request):
#     r = requests.get('http://127.0.0.1:8000/api')
#     data = r.json()
#     data = data['data'][0]
#     m = Test.objects.all()
#     if request.method == 'POST':
#         id = request.POST['test']
#         reverse_lazy('../api/?id=' + id)
#     return render(request, 'photo_gallery/pie.html', {'data': data, 'value': m})
