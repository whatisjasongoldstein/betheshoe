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


/* IMPROVED DEFER IMG
=====================
<img data-img-sizes="{&quot;50&quot;: &quot;small_thumb.jpg&quot;, &quot;500&quot;: &quot;medium.jpg&quot;, &quot;1000&quot;: &quot;big.jpg&quot; }">

This examines the size of the img object itself, and checks the 

*/
(function(){
    var images = $("[data-img-sizes]");
    images.each(function(i){
        var img = images[i];
        sizes = img.getAttribute('data-img-sizes');
        sizes = JSON.parse(sizes);
        var img_width = img.width;
        var new_src = img.src;
        var new_src_size = 0;
        for (key in sizes){
            key = parseInt(key, 10);
            if (key <= img_width && key > new_src_size){
                new_src = sizes[key];
                new_src_size = key;
            }
        }
        img.src = new_src;
    });
})();



