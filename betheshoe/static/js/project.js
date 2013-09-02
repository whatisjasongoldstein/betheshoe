// Enable tooltip on all tite'd links
$('a[title]').tooltip({});

$('#dropdown-btn').on("click", function(e){
    $(e.target).closest('.nav').find('.dropdown').toggleClass('active');
    return false;
});