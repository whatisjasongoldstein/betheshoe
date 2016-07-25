
def vimeo_id(url):
    if "vimeo.com/" in url:
        return url[url.find("vimeo.com/")+10:]
    return False

def vimeo_embed_url(url):
    """ Converts vimeo link to iframe src. """
    return "https://player.vimeo.com/video/%s" % vimeo_id(url) 
