const miBoton = document.querySelector("#boton-magico");

miBoton.addEventListener("click", function() {
    document.body.classList.toggle("noche");
});


//transición combinada con css//
const coches = document.querySelectorAll("article");

coches.forEach(function(coche){
    coche.addEventListener("click", function(){
        coche.classList.toggle("activo");
    });
});

