from django.shortcuts import render
from django .http import HttpResponse
from django.http import HttpResponseRedirect
from . models import userRegistration,productInformation
from . forms import registerForm,productForm

# Create your views here.

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        userLogin = userRegistration.objects.filter(username=username, password=password)
        if userLogin:
            return HttpResponse("hello")

    return render(request,'automaticShoppingCart/login.html')

def registrationpage(request):
    form = registerForm()
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']
            confirm_Password = form.cleaned_data['confirm_Password']

            uRD = userRegistration()

         
            uRD.username = username
            uRD.email = email
            uRD.password= password
            uRD.confirm_Password = confirm_Password
            uRD.mobile_number = mobile_number

            uRD.save()
            return render(request,'automaticShoppingCart/successful.html',{'form':form})
        
    return render(request,'automaticShoppingCart/registration.html',{'form':form})

def cart(request):
    cart_details = productInformation.objects.all()
    return render(request,'automaticShoppingCart/cart.html',{'cart_details':cart_details})


def deleteProduct(request,id):
    cart_data = productInformation.objects.get(id = id)
    cart_data.delete()
    cart_details = productInformation.objects.all()
    return render(request,'automaticShoppingCart/cart.html',{'cart_details':cart_details})