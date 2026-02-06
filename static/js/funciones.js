function ventana_cerrar() {
    const abrir_cerrar_caso = document.querySelectorAll(".cerrar_caso")
    const ventana_flotante = document.getElementById("ventana_flotante")
    const cancelar = document.getElementById("boton_cancelar")
    const cerrar =document.getElementById("boton_cerrar")

    abrir_cerrar_caso.forEach(eliminar=>{
        eliminar.addEventListener("click", ()=>{
            ventana_flotante.style.display="flex"
            if (ventana_flotante.style.display==="flex"){
                cancelar.addEventListener("click", ()=>{
                    ventana_flotante.style.display="none"
                })
            }
        })
    })
    
}

/**AQUI DESACTIVAMOS EL CAMPO FECHA SI EL COMPROMISO SE ENCUENTRA VACIO */

document.addEventListener("DOMContentLoaded", function() {
    const compromisoInput = document.querySelector("input[name='compromiso']");
    const fechaInput = document.querySelector("input[name='fecha_compromiso']");

    function toggleFecha() {
        if (compromisoInput.value.trim() === "") {
            fechaInput.disabled = true;
            fechaInput.value = "";
        } else {
            fechaInput.disabled = false;
        }
    }

    compromisoInput.addEventListener("input", toggleFecha);
    toggleFecha(); // inicializar estado
});

