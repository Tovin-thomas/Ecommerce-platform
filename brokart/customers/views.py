from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
from django.contrib.auth import authenticate,login,logout

def sign_out(request):
    logout(request)
    return redirect('account')

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
            try:
        

                username=request.POST.get('username')
                print(username)
                password=request.POST.get('password')
                email=request.POST.get('email')
                address=request.POST.get('address')
                phone=request.POST.get('phone')
                user=User.objects.create_user(username=username,password=password,email=email)
                customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
                                                )
                success_messages="USER REGISTERED SUCCESSFULLY"
                messages.success(request,success_messages)
            except Exception as e:
                error_messages="USER ALREADY EXIST"
                messages.error(request,error_messages)
               
           # return redirect('home')
       
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'user does not exist')
        
           

    return render(request,'account.html',context)