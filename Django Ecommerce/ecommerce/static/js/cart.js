var updateBtns = document.getElementsByClassName('update-cart')

// Roda um for dentro de todos os botões com essa classe e pega o id do produto e adiciona
for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            addCookieItem(productId, action);
            console.log("Usuário não está logado")
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}

// Manda os dados para o updateItem e transforma a resposta em json para recarregar a página
function updateUserOrder(productId, action){

    var url = '/update_item/'
    console.log('URL:', url)
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
     .then((response) => {
        return response.json();
      })

        .then((data) => {
        location.reload()
        });
}


function addCookieItem(productId, action){
    console.log('Usuário não está logado')

    if (action == 'add'){
        if (cart[productId] == undefined){
        cart[productId] = {'quantity':1}

        }else{
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0){
            console.log('Item foi deletado')
            delete cart[productId];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}