document.addEventListener("DOMContentLoaded", function () {

    const inputFecha = document.querySelector(
        'input[name="fecha_nacimiento_estud"]'
    );

    if (!inputFecha) return;

    const hoy = new Date();

    // Máximo permitido: hoy - 5 años
    const fechaMax = new Date(
        hoy.getFullYear() - 5,
        hoy.getMonth(),
        hoy.getDate()
    );

    // Mínimo permitido: hoy - 22 años
    const fechaMin = new Date(
        hoy.getFullYear() - 22,
        hoy.getMonth(),
        hoy.getDate()
    );

    const formatear = (fecha) => fecha.toISOString().split("T")[0];

    inputFecha.max = formatear(fechaMax);
    inputFecha.min = formatear(fechaMin);
});
