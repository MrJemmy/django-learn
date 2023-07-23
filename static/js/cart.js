console.log("CSRF :", csrftoken)
var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product // product : is Attribute of HTML
        var action = this.dataset.action     // action : is Attribute of HTML
        console.log('productId:',productId, 'action:',action)

        console.log('USER :',user)
        if(user == 'AnonymousUser'){
            addCookiItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookiItem(productId, action){
    console.log('AnonymousUser user, Not Logged In')

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity' : 1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }
    if(action == 'remove'){
        cart[productId]['quantity'] -= 1
        if(cart[productId]['quantity'] <= 0){
            console.log('Item should be deleted')
            delete cart[productId];
        }else{

        }
    }
    // overriting cart cooki in Browser
    console.log('cart : ', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
    location.reload()
}
function updateUserOrder(productId, action){
    console.log(user, 'Is Logged In')
    var url = 'add_item/'  // 'add_item/' working but '/add_item/' is not working
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({"productId":productId, "action":action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}