// Enable tooltip on all tite'd links
$('a[title]').tooltip({});

$('#dropdown-btn').on("click", function(e) {
    $(e.target).closest('.nav').find('.dropdown').toggleClass('active');
    return false;
});

$(document).on('click', '[data-open-id]', function(e) {
    var target = e.target.getAttribute('data-open-id');
    $(target).slideDown();
    return false;
});