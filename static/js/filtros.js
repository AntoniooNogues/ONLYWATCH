function updateYearDisplay(value) {
    document.getElementById('yearDisplay').textContent = value;
}

function updatePuntuacionDisplay(value) {
    document.getElementById('puntuacionDisplay').textContent = value;
}

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
        checkbox.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const labels = document.querySelectorAll('.dropdown-item label');

    labels.forEach(label => {
        label.addEventListener('click', function(event) {
            // Detén la propagación del evento para evitar que el dropdown se cierre
            event.stopPropagation();
        });
    });
});

let generosSeleccionados = [];
let plataformasSeleccionadas = [];

document.querySelectorAll('input[name="generos"]').forEach((checkbox) => {
    checkbox.addEventListener('change', function() {
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
    checkbox.addEventListener('change', function() {
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



function enviarDatosServidor() {
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            generos: generosSeleccionados,
            plataformas: plataformasSeleccionadas,
        }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.querySelectorAll('input[name="generos"], input[name="platformas"]').forEach((checkbox) => {
    checkbox.addEventListener('change', enviarDatosServidor);
});