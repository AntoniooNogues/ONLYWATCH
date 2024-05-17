// Funcion para desplegar los dropdowns de los filtros
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('informacion').style.display = 'none';
  });

  document.getElementById('mostrar-btn').addEventListener('click', function() {
    var informacion = document.getElementById('informacion');
    if (informacion.style.display === 'none') {
      informacion.style.display = 'block';
    } else {
      informacion.style.display = 'none';
    }
  });

  document.getElementById('cerrar').addEventListener('click', function() {
    document.getElementById('informacion').style.display = 'none';
  });

// Funcion para seleccionar y mostrar el año seleccionado para el filtro de año
function updateYearDisplay(year) {
    document.getElementById('yearDisplay').innerText = year;
}

 window.onload = function() {
        var yearSlider = document.getElementById('yearSlider');
        var maxYear = yearSlider.getAttribute('max');
        yearSlider.value = maxYear; // Establece el valor inicial en el máximo
        updateYearDisplay(maxYear); // Actualiza el año mostrado
    };

function  updateGenreDisplay(genre) {
    document.getElementById('genreDisplay').innerText = genre;
}

