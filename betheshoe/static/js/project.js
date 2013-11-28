// Enable tooltip on all tite'd links
$('a[title]').tooltip({});

$('#dropdown-btn').on("click touch", function(e) {
    $('.basement').slideToggle();
    return false;
});

$(document).on('click', '[data-open-id]', function(e) {
    var target = e.target.getAttribute('data-open-id');
    $(target).slideDown();
    return false;
});


// Setup get_params
(function(){
    window.get_params = window.get_params || {};
    var qpairs = window.location.search.slice(1).split("&");
    qpairs = _.map(qpairs, function(pair){
        return pair.split("=");
    });

    for (var i = qpairs.length - 1; i >= 0; i--) {
        get_params[qpairs[i][0]] = qpairs[i][1];
    };
}());

(function(){
    var jump = document.getElementById(window.get_params.jump);
    if (jump !== null) {
        document.onready = function(){
            window.scrollTo(0, jump.offsetTop);
        }
    };
})();