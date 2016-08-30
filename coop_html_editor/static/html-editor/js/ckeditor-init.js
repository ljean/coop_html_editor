CKEDITOR.disableAutoInline = true;
 
$(document).ready(function() {
    console.log('>>>> ck-editor-init');
    $('.inline-editable').attr('contenteditable', 'true');
    $('.inline-editable').each(function(index, elt) {
        var content_id = $(elt).attr('id');
        CKEDITOR.inline(content_id, {
            on: {
                blur: function( event ) {
                    var data = event.editor.getData();
                    $('#' + content_id + '_hidden').attr('value', data);
                }
            }
        });
    });
});