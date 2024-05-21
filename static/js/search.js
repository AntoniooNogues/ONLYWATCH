document.getElementById('search-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        window.location.href = '/buscar?buscar=' + encodeURIComponent(this.value);
    }
});