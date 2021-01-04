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
            console.log('usuario autenticado, enviando dados...')
        }


    })
}