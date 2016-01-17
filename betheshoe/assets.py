PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            "css/site.scss",
        ),
        'output_filename': 'css/app.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            "js/jquery.js",
            "js/underscore.js",
            "js/underscore.string.js",
            "js/modernizer.2.6.2.js",
            "js/tooltip.js",
            "js/project.js",
            "js/deferred-images.js",
        ),
        'output_filename': 'js/app.js',
    }
}
