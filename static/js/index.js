function togglePasswordVisibility(passwordId, buttonId) {
    var passwordInput = document.getElementById(passwordId);
    var eyeIcon = document.querySelector("#" + buttonId + " i");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");
    }
}

var togglePasswordVisibilityButton1 = document.getElementById("togglePasswordVisibility1");
if (togglePasswordVisibilityButton1) {
    togglePasswordVisibilityButton1.addEventListener("click", function(event) {
        event.stopPropagation();
        togglePasswordVisibility("password1", "togglePasswordVisibility1");
    });
}

var togglePasswordVisibilityButton2 = document.getElementById("togglePasswordVisibility2");
if (togglePasswordVisibilityButton2) {
    togglePasswordVisibilityButton2.addEventListener("click", function(event) {
        event.stopPropagation();
        togglePasswordVisibility("password2", "togglePasswordVisibility2");
    });
}


function decodeHtml(html) {
    var txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
}

document.addEventListener('DOMContentLoaded', function() {
    if (errores) {
        var decodedErrores = decodeHtml(errores);
        var erroresArray = JSON.parse(decodedErrores.replace(/'/g, '"'));
        var erroresElement = document.querySelector('.errores');
        var notificationElement = document.querySelector('.notification.is-danger.is-light');
        var deleteButton = document.querySelector('.delete');

        if (erroresArray.length !== 0) {
            erroresElement.textContent = erroresArray.join(', ');
            notificationElement.classList.remove('is-hidden');
        } else {
            notificationElement.classList.add('is-hidden');
        }

        // Add event listener to the delete button
        deleteButton.addEventListener('click', function () {
            notificationElement.classList.add('is-hidden');
        });
    }
});
