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

const filtrarButton = document.getElementById('filtrar');

let generosSeleccionadosId = 0;
let plataformasSeleccionadasId = 0;
let generosSeleccionadosName = '';
let plataformasSeleccionadasName = '';

document.querySelectorAll('input[name="generos"]').forEach((radio) => {
    radio.addEventListener('change', function () {
        if (this.checked) {
            generosSeleccionadosId = this.dataset.id;  // Use the data-id attribute
            generosSeleccionadosName = this.dataset.name;  // Use the data-name attribute
        }
    });
});

document.querySelectorAll('input[name="plataformas"]').forEach((radio) => {
    radio.addEventListener('change', function () {
        if (this.checked) {
            plataformasSeleccionadasId = this.dataset.id;  // Use the data-id attribute
            plataformasSeleccionadasName = this.dataset.name;  // Use the data-name attribute
        }
    });
});

filtrarButton.addEventListener('click', function () {
    let url = '/filtrar?';
    if (generosSeleccionadosName) {
        url += `generos=${generosSeleccionadosName}&`;
    }
    if (plataformasSeleccionadasName) {
        url += `plataformas=${plataformasSeleccionadasName}&`;
    }
    window.location.href = url;
});