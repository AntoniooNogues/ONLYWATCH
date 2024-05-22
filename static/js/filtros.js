document.addEventListener('DOMContentLoaded', function () {
    function toggleDropdown(event) {
        event.stopPropagation();
        const dropdown = event.currentTarget.closest('.dropdown');

        const dropdowns = document.querySelectorAll('.dropdown');
        dropdowns.forEach(drp => {
            if (drp !== dropdown) {
                drp.classList.remove('is-active');
            }
        });

        dropdown.classList.toggle('is-active');
    }

    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger button');

    dropdownTriggers.forEach(button => {
        button.addEventListener('click', toggleDropdown);
    });

    const checkboxes = document.querySelectorAll('.dropdown-item input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('click', function (event) {
            event.stopPropagation();
        });
    });
});

let generosSeleccionados = 0;
let plataformasSeleccionadas = 0;

const filtrarButton = document.getElementById('filtrar');

document.querySelectorAll('input[name="generos"]').forEach((radio) => {
    radio.addEventListener('change', function () {
        if (this.checked) {
            generosSeleccionados = this.value;  // Assign the value directly
        }
    });
});

document.querySelectorAll('input[name="plataformas"]').forEach((radio) => {
    radio.addEventListener('change', function () {
        if (this.checked) {
            plataformasSeleccionadas = this.value;  // Assign the value directly
        }
    });
});


filtrarButton.addEventListener('click', function () {
    let url = '/filtrar?';
    generosSeleccionados.push((genero) => {
        url += `generos=${genero}&`;
    });
    plataformasSeleccionadas.push((plataforma) => {
        url += `plataformas=${plataforma}&`;
    });
    window.location.href = url;
});