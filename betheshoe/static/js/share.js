(function(){
    /**
     * Facebook sharing
     */
    document.body.addEventListener("click", function(e){
        var share = e.target.getAttribute("data-share");
        if (share === null) {
            return;
        } else if (share === "") {
            share = window.location.href;
        }

        // Absolutize relative links
        if (share[0] === "/") {
            share = window.location.protocol+"//"+window.location.host + share;
        }

        var url = "https://www.facebook.com/sharer/sharer.php?u=" + share;
        window.open(url, "Share Be The Shoe", "width=600,height=400,top=100,left=100");

    });
})();