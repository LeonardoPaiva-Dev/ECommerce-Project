var updateButtons = document.getElementsByClassName('update-cart')

for(i = 0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product  
        var action = this.dataset.action
        console.log('productID: ', productId, 'Action: ', action)

        console.log('USER: ', user)
        if(user == 'AnonymousUser'){
            console.log('Usuario não autenticado')
        }
        else{
            updateUserOrder(productId, action)
        }


    })
}

function updateUserOrder(productId, action){
    console.log('Usuário esta logado, enviando dados...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((resposne) =>{
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
    })
}