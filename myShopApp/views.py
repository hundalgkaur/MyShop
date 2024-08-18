from django.shortcuts import render,redirect
from myShopApp.models import Contact,Product,Orders,OrderUpdate
from django.contrib import messages
from math import ceil
from MyShop.settings import RAZORPAY_SECRET_KEY,RAZORPAY_API_KEY
import razorpay
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_SECRET_KEY), auth_header='Bearer')

# Create your views here.
def index(request):

    allProds = []
    catprods = Product.objects.values('category','id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}

    return render(request,"index.html",params)
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email =request.POST.get("email")
        desc = request.POST.get("desc")
        phonenumber = request.POST.get("phonenumber")
        myquery = Contact(name=name,email=email,desc=desc,phonenumber=phonenumber)
        myquery.save()
        messages.info(request,"we will get back to you soon ")
        return render(request,"contact.html")

    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

def checkout(request):
   
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
# # PAYMENT INTEGRATION

        order_amount = 100  # Set the amount dynamically or based on your requirements
     
        order_currency= 'INR'
        payment_order=client.order.create(dict(amount=order_amount * 100,currency=order_currency,payment_capture=1))
        payment_order =payment_order['id']
        context ={
            'amount': 100 ,'api_key':RAZORPAY_API_KEY,'order_id':payment_order
        }
        

       
        return render(request, 'payment.html', context)


    return render(request, 'checkout.html')

# payment failure 
def payment_success_view(request):
   order_id = request.POST.get('order_id')
   payment_id = request.POST.get('razorpay_payment_id')
   signature = request.POST.get('razorpay_signature')
   params_dict = {
       'razorpay_order_id': order_id,
       'razorpay_payment_id': payment_id,
       'razorpay_signature': signature
   }
   try:
       client.utility.verify_payment_signature(params_dict)
       # Payment signature verification successful
       # Perform any required actions (e.g., update the order status)
       return render(request, 'payment_success.html')
   except razorpay.errors.SignatureVerificationError as e:
       # Payment signature verification failed
       # Handle the error accordingly
       return render(request, 'payment_failure.html')


