//var shipping = '{{order.shipping}}'
//console.log(shipping)
//var total = '{{order.get_cart_total|floatformat:2}}'

if (shipping == 'False'){
    document.getElementById("shipping-info").innerHTML = ''
}
if (user != 'AnonymousUser'){
    document.getElementById("user-info").innerHTML = ''
}
if (shipping == 'False' && user != 'AnonymousUser'){
    // Hide Entire Form if user is logged in and shipping info is false
    document.getElementById("form-wrapper").classList.add("hidden")
    // show payment if logged-in user wants to buy an item does not require shipping
    document.getElementById("payment-info").classList.remove("hidden")
}

var form = document.getElementById('form')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form Submitted...');
    document.getElementById("form-button").classList.add("hidden")
    document.getElementById("payment-info").classList.remove("hidden")
})

document.getElementById("make-payment").addEventListener('click', function(e){
    submitFormData()
})
function submitFormData(){
    console.log("payment button clicked")

    var userFormData = {
        'name' : null,
        'email' : null,
        'total' : total,
    }
    var shippingInfo = {
        'address' : null,
        'city' : null,
        'state' : null,
        'zipcode' : null,
    }

    if (user == 'AnonymousUser'){
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }
    if (shipping != 'False'){
        shippingInfo.address = form.address.value
        shippingInfo.city = form.city.value
        shippingInfo.state = form.state.value
        shippingInfo.zipcode = form.zipcode.value
    }
    var url = 'process_order/'  // 'process_order/' working but '/process_order/' is not working
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({"form":userFormData, "shipping":shippingInfo})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('Success:', data);
        alert('Transaction completed');

        cart = {}
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
        console.log('store url',store)
        window.location.href = store
    })
}