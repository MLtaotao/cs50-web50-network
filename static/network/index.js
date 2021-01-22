document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('#newpost-btn')) {
        document.querySelector('#newpost-btn').addEventListener('click', show_newpost);
    }

});


function show_newpost() {
    if (document.querySelector('#newpost-btn').innerHTML == 'New Post') {
        document.querySelector('#newpost').style.display = 'block';
        document.querySelector('#newpost-btn').className = "btn btn-secondary";
        document.querySelector('#newpost-btn').innerHTML = 'Hide';
    }
    else {
        document.querySelector('#newpost').style.display = 'none';
        document.querySelector('#newpost-btn').innerHTML = 'New Post';
        document.querySelector('#newpost-btn').className = "btn btn-primary";
    }
}

