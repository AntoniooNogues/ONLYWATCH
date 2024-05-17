// Funcion para desplegar los dropdowns de los filtros
document.addEventListener('DOMContentLoaded', function () {
    var dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(function (dropdown) {
        dropdown.querySelector('.dropdown-trigger button').addEventListener('click', function () {
            dropdown.classList.toggle('is-active');
        });
    });
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

function updateYearDisplay(year) {
    document.getElementById('yearDisplay').innerText = year;
}