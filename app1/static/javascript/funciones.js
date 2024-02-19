function contacto(){

    window.addEventListener('scroll',()=>{var scroll=
        document.documentElement.scrollTop;
    console.log(scroll);
    var botonarriba= document.getElementById('contactanos');
    if(scroll>940){
      contactanos.style.right= 150+"px";
    }
    if(scroll<940){
      contactanos.style.right= -550+"px";
    }
    })
}
function datos(){
  var email=document.getElementById("email").value
  if (email.length==0){
    alert("Escriba su correo");
              }
 
  ;
  var numero=document.getElementById("numero").value
  if (numero.length==0){
    alert(" agreegue un numero telefonico");
              };
  var mensaje=document.getElementById("coment").value
  if (mensaje.length==0){
    alert(" agreegue algun mensaje para enviar");
              }
  ;
  
}
