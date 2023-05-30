console.log("CSRF :", csrftoken)
var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product // product : is Attribute of HTML
        var action = this.dataset.action     // action : is Attribute of HTML
        console.log('productId:',productId, 'action:',action)

        console.log('USER :',user)
        if(user == 'AnonymousUser'){
            console.log('AnonymousUser user, Not Logged In')
        }else{
            updateUserOrder(productId, action)
        }
    })
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