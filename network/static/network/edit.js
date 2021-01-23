document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#post-edit-button').forEach(button => {
        button.onclick = function() {
            let edit_area = button.parentElement.querySelector('#post-body');
            var post_id = this.dataset.post_id;
            var value = edit_area.innerHTML;
            edit_area.innerHTML = `
                <form id="edit-form">
                    <textarea id="editor1" name="editor1">${value}</textarea>
                    <div style="text-align: right;">
                        <button type="submit" class="btn btn-primary btn-sm">Submit</button>
                        <button type="button" id="cancel" class="btn btn-secondary btn-sm">Cancel</button>     
                    </div>
                </form>
                `
            button.style.visibility = 'hidden';
            edit_form = edit_area.querySelector('#edit-form');
            cancel_button = edit_area.querySelector('#cancel');
            cancel_button.onclick = function() {
                edit_area.innerHTML = value;
                button.style.visibility = 'visible';
            }
            var editor = CKEDITOR.replace('editor1');

            // fetch edit form to view
            edit_form.onsubmit = function() {
                let data = {
                    'post_id': post_id,
                    'edit_body': editor.getData(),
                };
                let csrftoken = getCookie('csrftoken');
                // console.log(data)
                fetch('/edit_post', {
                    method: 'POST',
                    body: JSON.stringify(data),
                    headers: { "X-CSRFToken": csrftoken },
                })
                .then(response => response.json())
                .then(result => {
                    // Print result
                    console.log(result);
                });
                location.reload();
                return false;
            }
            
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}