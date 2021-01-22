document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#post-edit-button').forEach(button => {
        button.onclick = function() {
            console.log(this.dataset.post_id);
            var edit_area = document.createElement('input');
            setAttributes(edit_area, {"name": "editor", "class": "ckeditor", "type": "text", "row": "3", "col": "10"});
            CKEDITOR.replace(edit_area);
            button.after(edit_area)
            button.style.visibility = 'hidden';
        }
    });
});


function setAttributes(el, attrs) {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
  }