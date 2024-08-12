from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                messages.info(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email)
        user.is_active=False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })

        email_from = settings.EMAIL_HOST_USER
        reci_list = [user.email,]



        def send_mail(email_subject, message, email_from, reci_list):
    """
    Send an email to a list of recipients.

    Args:
        email_subject (str): The subject of the email.
        message (str): The body of the email.
        email_from (str): The sender's email address.
        reci_list (list): A list of recipient email addresses.

    Returns:
        None
    """

        # Create a message container
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = ', '.join(reci_list)
        msg['Subject'] = email_subject

         # Attach the message to the container
        msg.attach(MIMEText(message, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP('your_smtp_server', 587)
        server.starttls()
        server.login(email_from, 'your_password')

        # Send the email
        text = msg.as_string()
        server.sendmail(email_from, reci_list, text)
        server.quit()

        # Example usage:
        email_subject = "Hello from Python!"
     message = "This is a test email sent from Python."
     email_from = "gkhundal0001@gmail.com"
     reci_list = ["gkhundal0001@gmail.com,gkhundal00001@gmail.com"]

        send_mail(email_subject, message, email_from, reci_list)
        messages.success(request,f"Activate Your Account by clicking the link in your gmail {message}")
        return redirect('/auth/login/')
    return render(request,"signup.html")


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activatefail.html')
def hundlelogin(request):
    return render(request,"login.html")
def hundlelogout(request):
    return redirect('/auth/login')