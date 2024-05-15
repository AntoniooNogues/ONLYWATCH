document.addEventListener("DOMContentLoaded", function() {
    const searchIcon = document.getElementById('search-icon');
    const searchContainer = document.getElementById('search-container');

    searchIcon.addEventListener('click', function() {
        searchContainer.classList.toggle('is-hidden');
    });
});
