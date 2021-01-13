document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#newpost-btn').addEventListener('click', show_newpost);
    
    all_post();
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

function all_post() {
    fetch("/all")
    .then(response => response.json())
    .then(posts => {
        posts.forEach(post => {
            var datetime = new Date(post.post_time);
            var post_object = document.createElement('div');
            post_object.className= "card text-center";
            post_object.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${post.poster}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${datetime.toLocaleString()}</h6>
                ${post.body}
                <a href="#" class="card-link">Like</a>
                <a href="#" class="card-link">Unlike</a>
            </div>
            `
            post_object.getElementsByClassName("card-title")[0].addEventListener('click', () => view_profile(post.poster), false);

            document.querySelector('#all-post').appendChild(post_object);

        });
    });
}

function view_profile(user) {
    console.log(user);
}