function adjustHeroSize() {
        var screenWidth = window.innerWidth;
        var heroElement = document.querySelector('main.hero');

        if (screenWidth >= 1920) {
            heroElement.classList.remove('is-small');
            heroElement.classList.add('is-medium');
        } else {
            heroElement.classList.remove('is-medium');
            heroElement.classList.add('is-small');
        }
    }

    // Llama a la función cuando se carga la página y cuando se cambia el tamaño de la ventana
    window.addEventListener('DOMContentLoaded', adjustHeroSize);
    window.addEventListener('resize', adjustHeroSize);