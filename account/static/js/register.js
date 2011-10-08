$(document).ready(function(){
    $('#sign_up_form').submit(function() {
        validate($(this));
        return false;
    });
});