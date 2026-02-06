// Espera a que toda la página cargue
document.addEventListener("DOMContentLoaded", function() {
    // Seleccionamos el input de fecha por name (o ID si lo prefieres)
    const inputFecha = document.querySelector("input[name='fecha_compromiso']");

    // Si no existe, no hacemos nada
    if (!inputFecha) return;

    // Obtenemos mañana
    const hoy = new Date();
    hoy.setDate(hoy.getDate() + 1);

    // Formateamos YYYY-MM-DD
    const yyyy = hoy.getFullYear();
    const mm = String(hoy.getMonth() + 1).padStart(2, '0');
    const dd = String(hoy.getDate()).padStart(2, '0');

    const fechaMin = `${yyyy}-${mm}-${dd}`;

    // Aplicamos la fecha mínima al input
    inputFecha.setAttribute("min", fechaMin);
});
