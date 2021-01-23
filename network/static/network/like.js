document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelectorAll('#post-like')) {
        document.querySelectorAll('#post-like').forEach(a => {
            a.onclick = function() {
                console.log(this.dataset.post_id);
                var post_id = this.dataset.post_id;
                let data = {
                    'post_id': post_id,
                };
                let csrftoken = getCookie('csrftoken');
                fetch('/like_post', {
                    method: 'PUT',
                    body: JSON.stringify(data),
                    headers: { "X-CSRFToken": csrftoken },
                })
                .then(response => response.json())
                .then(result => {
                    // Print result
                    console.log(result);
                });
                location.reload();
                // return false;
            }
        })
    }

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