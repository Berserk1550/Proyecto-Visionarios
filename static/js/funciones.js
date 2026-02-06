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

function buscadorDeArticulos() {
    document.addEventListener("keyup", e => {
        if (e.target.matches("#barra_busqueda")) {

            const filas = document.querySelectorAll("#informacion");
            let coincidencias = 0;

            filas.forEach(fila => {
                const texto = fila.textContent.toLowerCase();
                const busqueda = e.target.value.toLowerCase();

                if (texto.includes(busqueda)) {
                    fila.style.display = "";
                    coincidencias++;
                } else {
                    fila.style.display = "none";
                }
            });

            let mensaje = document.getElementById("mensaje_no_encontrado");

            if (!mensaje) {

                e.target.parentNode.appendChild(mensaje);
            }

            if (coincidencias === 0) {
                mensaje.style.display = "block";
            } else {
                mensaje.style.display = "none";
            }
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    ventana_cerrar();

    if (document.getElementById("barra_busqueda")) {
        buscadorDeArticulos();
    }
});

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


