from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here
def signup(request):
    print("i am running the  signup function ")
    if(request.method =="POST"):
        print("IT IS POST REQUEST")
        email=request.POST['email']
        passsword=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if passsword != confirm_password:
            messages.warning(request,"Password is not matching")
            #return HttpResponse("password wrong")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exit")
              
                
        except Exception as identifier:
            pass
        #user =User.objects.create_user(email,email,password)
        new_user = User.objects.create_user(email, email)
        new_user.save()
        return HttpResponse('user created',email)

    return render(request,"signup.html")

def hundlelogin(request):
    return render(request,"login.html")
def hundlelogout(request):
    return redirect('/auth/login')