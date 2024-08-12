from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.hundlelogin,name='hundlelogin'),
    path('logout/',views.hundlelogout,name='hundlelogout'),

    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    
]
