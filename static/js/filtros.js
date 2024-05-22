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



let generosSeleccionados = [];
let plataformasSeleccionadas = [];



const filtrarButton = document.getElementById('filtrar');

document.querySelectorAll('input[name="generos"]').forEach((checkbox) => {
    checkbox.addEventListener('change', function () {
        if (this.checked) {
            generosSeleccionados.push(this.value);
        } else {
            var index = generosSeleccionados.indexOf(this.value);
            if (index !== -1) {
                generosSeleccionados.splice(index, 1);
            }
        }
    });
});

document.querySelectorAll('input[name="platformas"]').forEach((checkbox) => {
    checkbox.addEventListener('change', function () {
        if (this.checked) {
            plataformasSeleccionadas.push(this.value);
        } else {
            var index = plataformasSeleccionadas.indexOf(this.value);
            if (index !== -1) {
                plataformasSeleccionadas.splice(index, 1);
            }
        }
    });
});


filtrarButton.addEventListener('click', function () {
    let url = '/filtrar?';
    generosSeleccionados.forEach((genero) => {
        url += `generos=${genero}&`;
    });
    plataformasSeleccionadas.forEach((plataforma) => {
        url += `plataformas=${plataforma}&`;
    });
    window.location.href = url;
});