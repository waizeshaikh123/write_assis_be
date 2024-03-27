from django.shortcuts import render,HttpResponse
from write_assis.models import Login
from write_assis.models import Sign

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reviews(request):
    return render(request, 'reviews.html')

def About(request):
    return render(request, 'about.html')

def hto(request):
    return render(request, 'how_to_order.html')

def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password=request.POST['password']
        sa = Login(email=email, password=password)
        sa.save()
        print("Save Success")
    return render(request, 'login.html')

def sign_up(request):
    if request.method=="POST":
        email = request.POST['email']
        password=request.POST['password']
        sa = Sign(email=email, password=password)
        sa.save()
        print("Save Success")
    return render(request, 'sign_up.html')
