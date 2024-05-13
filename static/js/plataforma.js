document.addEventListener('DOMContentLoaded', function () {
    const imagenesPlataforma = document.querySelectorAll('.plataforma-imagen');
    imagenesPlataforma.forEach(function (imagen) {
        imagen.addEventListener('click', function () {
            const plataformaId = imagen.id.split('_')[1];
            window.location.href = "vincular_desvincular_plataforma/" + plataformaId + "/"; // Redirigir con el ID de la plataforma
        });
    });
});
