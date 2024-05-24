// <---! Vincular peliculas con generos --->
document.addEventListener('DOMContentLoaded', function () {
    const iconosGenero = document.querySelectorAll('.toggle-genre');
    iconosGenero.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            console.log(enlace.dataset.genreId); // Imprimir el valor de data-genreId
            const generoId = enlace.id;
            const peliculaId = document.getElementById('movieId').value;
            url = '/administrador/pelicula/vincular_pelicula/vincular_genero/'
            window.location.href = url + peliculaId + "?generoId=" + generoId;
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
            window.location.href = "/administracion/pelicula/vincular_pelicula/vincular_plataforma/" + peliculaId +  "?plataformaId=" + plataformaId;
        });
    });
});

// <---! Vincular series con generos --->
document.addEventListener('DOMContentLoaded', function () {
    const iconosGenero = document.querySelectorAll('.genero');
    iconosGenero.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            console.log(enlace.dataset.genreId); // Imprimir el valor de data-genreId
            const generoId = enlace.id;
            const serieId = document.getElementById('serieId').value;
            console.log(serieId);
            url = '/administrador/serie/vincular_serie/vincular_genero/'
            window.location.href = url + serieId + "?generoId=" + generoId;
        });
    });
});

// <---! Vincular series con plataformas --->
document.addEventListener('DOMContentLoaded', function () {
    const Plataforma = document.querySelectorAll('.plataforma-idd');
    Plataforma.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            const plataformaId = enlace.id;
            const serieId = document.getElementById('serieId').value;
            window.location.href = "/administracion/serie/vincular_serie/vincular_plataforma/" + serieId +  "?plataformaId=" + plataformaId;
        });
    });
});



