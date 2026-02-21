(function () {
    function initArticleEditor() {
        if (!window.tinymce) return;

        if (window.tinymce.get('id_content')) {
            window.tinymce.remove('.richtext-editor');
        }

        window.tinymce.init({
            selector: 'textarea.richtext-editor',
            menubar: 'file edit view insert format table tools help',
            plugins: 'lists link image table code fullscreen wordcount searchreplace',
            toolbar: [
                'undo redo | blocks | bold italic underline strikethrough |',
                'alignleft aligncenter alignright alignjustify | bullist numlist outdent indent |',
                'link image table | removeformat | code fullscreen'
            ].join(' '),
            block_formats: 'Paragraph=p; Heading 1=h1; Heading 2=h2; Heading 3=h3; Heading 4=h4',
            height: 380,
            branding: false,
            promotion: false,
            convert_urls: false,
            image_title: true,
            automatic_uploads: false,
            setup: function (editor) {
                editor.on('change keyup', function () {
                    editor.save();
                });
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initArticleEditor);
    } else {
        initArticleEditor();
    }
})();
