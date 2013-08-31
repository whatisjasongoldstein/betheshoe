// DEFER URL LOAD
(function(){

    var insert_content = function(data, textStatus, jqXHR){
        var placeholders = $('[data-deferred-load="'+this.url+'"]');
        for (var i = placeholders.length - 1; i >= 0; i--) {
            placeholders[i].innerHTML += data;
        }
    };

    var load_data = function(placeholder){
        $.ajax({
            url: $(placeholder).attr('data-deferred-load'),
            type: 'GET',
            format: 'jsonp',
            timeout : 10000,
            success: insert_content
        });
    };

    var placeholders = $('[data-deferred-load]');
    placeholders.each(function(i){
        load_data(placeholders[i]);
    });

})();

// DEFER IMG
(function(){

    var change_src = function(element){
        var deferred = $(element).attr('data-deferred-src');
        element.src = deferred;
    };

    var images = $('[data-deferred-src]');
    images.each(function(i){
        var pageWidth = document.width || document.body.clientWidth; // IE is stupid.
        if (pageWidth > 700) { // Unnecessary for small devices.
            change_src(images[i]);
        }
    });


})();