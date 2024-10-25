//representa o botão de menu de cçasse ceçlular no HTML
var iconeMenu= document.querySelector('.celular');
//representando a lista do menu que está invisivel
var listaMenu= document.querySelector('.opcoes');

//monitora icone do menu, se está tendo algum clique 
iconeMenu.addEventListener('click',function() {
 //alternar classe "opcoes" para "mostrarMenu"
listaMenu.classList.toggle('mostrarMenu');

});
