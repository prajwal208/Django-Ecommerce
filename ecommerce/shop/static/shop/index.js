//cart function



//Get item in the cart



//Increment cart item value onclick

$('.cart').click(function(){
    let name    
    var idstr= this.id.toString();
    console.log(idstr);
    if(cart[idstr]!= undefined) {
    qty = cart[idstr][0]+1;
    }
    else{
    qty = 1;
    if(document.getElementById('name')!=null){
    name=document.getElementsByClassName('card-title' + idstr).innerHTML
    }
    cart[idstr]= [qty,name]
    }
    updateCart(cart)
    console.log(cart);
});

//update cart value
const updateCart = (cart) => {
    sum = 0
    for (var item in cart) {
        sum = sum + cart[item][0]
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover()
}  

if(localStorage.getItem('cart') == null){
    var cart = {}
}
else{
    cart = JSON.parse(localStorage.getItem('cart'))
    updateCart(cart)
}



//update cart popover


updatePopover(cart);
function updatePopover(cart) {
    $('#popcart').tooltip;
}

const clearcart = () => {
    cart = JSON.parse(localStorage.getItem('cart'))
    for(var item in cart){
        document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>'
    }
    localStorage.clear()
    cart = {}
    updateCart(cart)
}








//----------value incrementer in cart----------------
$('.divprod').on("click", "button.minus", function() {
    a = this.id.slice(7, );
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});

$('.divprod').on("click", "button.plus", function() {
    a = this.id.slice(6, );
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});