document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#post-edit-button').forEach(button => {
        button.onclick = function() {
            console.log(this.dataset.post_id);
            var edit_area = document.createElement('input');
            CKEDITOR.relpace()

        }
    });
});