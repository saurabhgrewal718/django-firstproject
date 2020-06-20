from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return render(request,'register.html')
            else:
                user= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password dont match')
            return render(request,'register.html')

    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')