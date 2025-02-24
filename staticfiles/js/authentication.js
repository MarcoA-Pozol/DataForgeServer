$(document).ready(function () {
    // Display Register or Login formularies.
    $('#button-display-register').on('click', function () {
        $('#login-form').removeClass('login-form').addClass('hidden-container');
        $('#register-form').removeClass('hidden-container').addClass('register-form');
    });
    
    $('#button-display-login').on('click', function () {
        $('#register-form').removeClass('register-form').addClass('hidden-container');
        $('#login-form').removeClass('hidden-container').addClass('login-form');
    });


    // Show message when new user is just registered.
    // Include JQuery code here...
});