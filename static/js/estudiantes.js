document.addEventListener("DOMContentLoaded", function() {

  // ------------------------------
  // Confirmación antes de eliminar
  // ------------------------------
    const formulariosEliminar = document.querySelectorAll('form[action^="/admin/eliminar_estudiante/"]');

    formulariosEliminar.forEach(form => {
        form.addEventListener('submit', function(e) {
        e.preventDefault(); // Evita envío inmediato

        Swal.fire({
            title: '¿Estás seguro?',
            text: "¡No podrás revertir esto!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, retirar estudiante!',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
            form.submit(); // Envía el formulario si confirma
            }
        });
        });
    });

    // ------------------------------
    // Mensaje de éxito si se eliminó un estudiante
    // ------------------------------
    const urlParams = new URLSearchParams(window.location.search);
    if(urlParams.get('deleted') === '1'){
        Swal.fire({
        title: '¡Retirado!',
        text: 'El estudiante ha sido retirado correctamente.',
        icon: 'success',
        confirmButtonColor: '#3085d6'
        }).then(() => {
        // Quita el parámetro de la URL para que no vuelva a mostrar la alerta
        const newUrl = window.location.href.split('?')[0];
        window.history.replaceState({}, document.title, newUrl);
        });
    }

});
