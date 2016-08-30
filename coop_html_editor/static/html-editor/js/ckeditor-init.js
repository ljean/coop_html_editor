CKEDITOR.disableAutoInline = true;
 
var adaptDroppedElement = function () {
    $(".inline-editable img.library-thumbnail").each(function(idx, elt) {
      $(elt).removeClass("library-thumbnail");
      $(elt).attr("src", $(elt).attr("rel"));
      $(elt).attr("data-cke-saved-src", $(elt).attr("rel"));
      $(elt).removeAttr('rel');
    });

    $(".inline-editable img.library-document").each(function(idx, elt) {
      var doc_url = $(elt).attr('rel');
      var doc_title = $(elt).attr('title');
      var icon_url = $(elt).attr('src');
      var doc_ext = icon_url.replace(/\\/g,'/').replace( /.*\//, '').replace('.png', '');
      var link = '<a href="'+doc_url+'" target="_blank" class="doc-link" rel="'+doc_ext+'">'+'<img src="'+icon_url+'" /><span class="doc-title">'+doc_title+'</span></a>';
      $(link).insertAfter($(elt));
      $(elt).remove();
    });
};

var saveInlineEditorData = function(editorId, editorElt) {
    var data = editorElt.getData();
    $('#' + editorId + '_hidden').attr('value', data);
};

$(document).ready(function() {
    $('.inline-editable').attr('contenteditable', 'true');
    $('.inline-editable').each(function(index, elt) {
        var editorId = $(elt).attr('id');
        CKEDITOR.inline(editorId, {
            on: {
                change: function( event ) {
                    saveInlineEditorData(editorId, event.editor);
                },
                drop: function (event) {
                    setTimeout(function() {
                        adaptDroppedElement();
                        saveInlineEditorData(editorId, event.editor);
                    }, 100);
                }
            }
        });
    });
});