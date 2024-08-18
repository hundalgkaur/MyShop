$(document).ready(function(){
    $('#rzp-button1').click(function(e){
      e.preventDefault();
      var fname = $('[name="name"]').val();
      var email = $('[name="email"]').val();
      var address1 = $('[name="address1"]').val();
      var address2 = $('[name="address2"]').val();
      var city = $('[name="city"]').val();
      var state = $('[name="state"]').val();
      var zip_code = $('[name="zip_code"]').val();
      var phone = $('[name="phone"]').val();
  
      if(fname == "" || email == "" || address1 == "" || address2 == "" || city == "" || state == "" || zip_code == "" || phone == ""){
        alert("All fields are mandatory");
        return false;
      } else {
        var options = {
          key: 'YOUR_KEY_ID', // Enter the Key ID generated from the Dashboard
          amount: '50000', // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
          currency: 'INR',
          name: 'Acme Corp', // your business name
          description: 'Test Transaction',
          image: 'https://example.com/your_logo',
          order_id: 'order_9A33XWu170gUtm', // This is a sample Order ID. Pass the `id` obtained in the response of Step 1
          handler: function(response){
            alert(response.razorpay_payment_id);
            alert(response.razorpay_order_id);
            alert(response.razorpay_signature);
          },
          prefill: {
            name: fname, // use the user's name
            email: email, // use the user's email
            contact: phone // use the user's phone number
          },
          notes: {
            address: address1 + ', ' + address2 + ', ' + city + ', ' + state + ', ' + zip_code
          },
          theme: {
            color: '#3399cc'
          }
        };
  
        var rzp1 = new Razorpay(options);
  
        rzp1.on('payment.failed', function(response){
          alert(response.error.code);
          alert(response.error.description);
          alert(response.error.source);
          alert(response.error.step);
          alert(response.error.reason);
          alert(response.error.metadata.order_id);
          alert(response.error.metadata.payment_id);
        });
  
        rzp1.open();
      }
    });
  });