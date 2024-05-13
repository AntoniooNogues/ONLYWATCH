// <---! Vincular peliculas con generos --->
document.addEventListener('DOMContentLoaded', function () {
    const iconosGenero = document.querySelectorAll('.toggle-genre');
    iconosGenero.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            console.log(enlace.dataset.genreId); // Imprimir el valor de data-genreId
            const generoId = enlace.id;
            const peliculaId = document.getElementById('movieId').value;
            window.location.href = "administrador/pelicula/vincular_pelicula/vincular_genero/" + peliculaId + "?generoId=" + generoId;
        });
    });
});

// <---! Vincular peliculas con plataformas --->
document.addEventListener('DOMContentLoaded', function () {
    const Plataforma = document.querySelectorAll('.plataforma-id');
    Plataforma.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            const plataformaId = enlace.id;
            const peliculaId = document.getElementById('movieId').value;
            window.location.href = "administrador/pelicula/vincular_pelicula/vincular_plataforma/" + peliculaId +  "?plataformaId=" + plataformaId;
        });
    });
});

