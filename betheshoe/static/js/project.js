// Enable tooltip on all tite'd links
$('*[title]').tooltip({});

$('#dropdown-btn').on("click touch", function(e) {
    $('.basement').slideToggle();
    return false;
});

$(document).on('click', '[data-open-id]', function(e) {
    var target = e.target.getAttribute('data-open-id');
    $(target).slideDown();
    return false;
});
