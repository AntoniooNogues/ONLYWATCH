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