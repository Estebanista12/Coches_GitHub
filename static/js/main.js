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



const modal = document.getElementById("miModal");
const btnAbrir = document.getElementById("btnAbrir");
const btnCerrar = document.getElementById("btnCerrar");

btnAbrir.addEventListener("click", () => {
  modal.style.display = "block";
});

btnCerrar.addEventListener("click", () => {
  modal.style.display = "none";
});

// cerrar haciendo clic fuera del contenido
window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});


const boton = document.getElementById("btnOcultar");
const texto = document.getElementById("title");

boton.addEventListener("click", () => {
  texto.style.display = "none";
});
