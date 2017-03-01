$(document).ready(function(){
    $('.parallax').parallax();
    $('.carousel').carousel();


    var $toastContent = $('{{request.session.toast}}');
    Materialize.toast($toastContent, 5000);

});
