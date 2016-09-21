# -*- coding: utf-8 -*-
"""view for aloha editor"""

import json

from django.shortcuts import render
from django.http import HttpResponse

from . import settings
from .utils import get_model


def html_editor_init(request):
    """
    Build the javascript file which is initializing the aloha-editor
    Run the javascript code for the AlohaInput widget
    """
    
    links = []
    for full_model_name in settings.link_models():
        app_name, model_name = full_model_name.split('.')
        model = get_model(app_name, model_name)
        if model:
            links.extend(model.objects.all())

    editors_config = {
        'aloha': {
            'jquery_no_conflict': settings.jquery_no_conflict(),
            'sidebar_disabled': 'true' if settings.sidebar_disabled() else 'false',
            'css_classes': settings.css_classes(),
            'resize_disabled': settings.resize_disabled(),
        },
        'ck-editor': {
            'css_classes': settings.css_classes(),
        }
    }

    editor_name = settings.get_html_editor()
    editor_config = editors_config.get(editor_name, None)

    return render(
        request,
        settings.init_js_template(),
        {
            'links': links,
            'config': editor_config,
        },
        content_type='text/javascript'
    )


def ckeditor_config(request):
    return render(
        request,
        'html_editor/ckeditor_config.js',
        {

        },
        content_type='text/javascript'
    )


def browser_urls(request):

    links = []
    for full_model_name in settings.link_models():
        app_name, model_name = full_model_name.split('.')
        model = get_model(app_name, model_name)
        if model:
            links.extend(model.objects.all())

            """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example: Browsing Files</title>
    <script>
        // Helper function to get parameters from the query string.
        function getUrlParam( paramName ) {
            var reParam = new RegExp( '(?:[\?&]|&)' + paramName + '=([^&]+)', 'i' );
            var match = window.location.search.match( reParam );

            return ( match && match.length > 1 ) ? match[1] : null;
        }
        // Simulate user action of selecting a file to be returned to CKEditor.
        function returnFileUrl() {

            var funcNum = getUrlParam( 'CKEditorFuncNum' );
            var fileUrl = '/path/to/file.txt';
            window.opener.CKEDITOR.tools.callFunction( funcNum, fileUrl );
            window.close();
        }
    </script>
</head>
<body>
    <button onclick="returnFileUrl()">Select File</button>
</body>
</html>
            """

            #window.opener.CKEDITOR.tools.callFunction(funcNum, fileUrl[, data] );

    return HttpResponse(json.dumps(links), content_type='text/javascript')


def browser_images(request):
    return render(
        request,
        'html_editor/ckeditor_config.js',
        {

        },
        content_type='text/javascript'
    )