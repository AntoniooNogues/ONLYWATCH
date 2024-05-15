document.getElementById('search-button').addEventListener('click', function() {
    var searchQuery = document.getElementById('search-input').value;
    if (searchQuery) {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/search_redirect/', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));  // Asegúrate de tener una función que obtenga la cookie CSRF
        xhr.send('q=' + encodeURIComponent(searchQuery));
    }
});