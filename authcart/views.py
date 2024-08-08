from django.shortcuts import render,redirect

# Create your views here.
# Create your views here.
def signup(request):
    return render(request,"authentication/signup.html")
def hundlelogin(request):
    return render(request,"authentication/login.html")
def hundlelogout(request):
    return redirect('/auth/login')