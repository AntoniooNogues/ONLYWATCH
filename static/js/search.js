document.getElementById('search-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        window.location.href = '/buscar?buscar=' + encodeURIComponent(this.value);
    }
});

// Aplica al navbar que se encuentra en la gran mayoria de las paginas.
var navbar = document.querySelector('.navbar-menu');
function toggleNavbar() {
    if (navbar.style.display === "none") {
        navbar.style.display = "block";
    } else {
        navbar.style.display = "none";
    }
}
document.getElementById('toggleNavbarButton').addEventListener('click', toggleNavbar);
