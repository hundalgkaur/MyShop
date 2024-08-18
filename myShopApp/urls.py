from django.urls import path
from myShopApp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('checkout/',views.checkout,name="checkout"),
    path('payment/success/',views.payment_success_view, name='payment_success'),
]
