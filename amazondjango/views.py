from django.shortcuts import render,redirect, get_object_or_404
from django.conf import settings
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ProductTV, ProductPictureTV, ProductType, ProductShofa, ProductPictureShofa, ProductReview, CarouselTV1, CarouselTV2
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def listingshofa(request):
    queryset_list = ProductShofa.objects.all()

    paginator = Paginator(queryset_list, 2)

    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'listingshofa.html', {'page_obj': queryset})

def listingtv(request):
    queryset_list = ProductTV.objects.all()

    paginator = Paginator(queryset_list, 2)

    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'listingtv.html', {'page_obj1': queryset})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'register.html',
                          {'user_form':user_form,
                           'registered':registered})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
    
def producttv(request, id):
    producttv = get_object_or_404(ProductTV, pk=id)
    prodtype = producttv.product_type
    tv = ProductTV.objects.filter(product_type=prodtype)
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        rp = ProductReview(
            product = producttv,
            customer_review = review,
            customer_rating = rating
        )

        rp.save()
        
    return render(request, 'producttv.html', {
        'producttv':producttv,
        'product_tv_type':tv,
    })

def productshofa(request, id):
    productshofa = get_object_or_404(ProductShofa, pk=id)
    prodtype = productshofa.product_type
    shofa = ProductShofa.objects.filter(product_type=prodtype)
    
    return render(request, 'productshofa.html', {
        'productshofa':productshofa,
        'product_shofa_type':shofa
    })

def SearchResultView(request):
    model_tv = ProductTV
    model_shofa = ProductShofa
    template_name = 'search_result.html'
    query = request.GET.get('q')
    object_list = ProductTV.objects.filter(name__icontains=query)
    obj_shofa = ProductShofa.objects.filter(name__icontains=query)
        
    return render(request, 'search_result.html',{
        'object_list':object_list,
        'obj_shofa':obj_shofa,
        'query' : query,
        
    })
