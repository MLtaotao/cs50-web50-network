document.addEventListener('DOMContentLoaded', function() {
    if(document.querySelector('#profile_follow')) {
        var follow_button = document.querySelector('#profile_follow');
        var profile_id = follow_button.getAttribute('data-profile_id');
        var user_id = follow_button.getAttribute('data-user_id');
        follow_button.addEventListener('click', () => follow(profile_id, user_id));
    }

    if(document.querySelector('#profile_unfollow')) {
        var unfollow_button = document.querySelector('#profile_unfollow');
        var profile_id = unfollow_button.getAttribute('data-profile_id');
        var user_id = unfollow_button.getAttribute('data-user_id');
        unfollow_button.addEventListener('click', () => unfollow(profile_id, user_id));
    }
});


function follow(profile_id, user_id) {
    fetch(`/follow/${profile_id}/${user_id}`);
    location.reload();
}

function unfollow(profile_id, user_id) {
    fetch(`/unfollow/${profile_id}/${user_id}`);
    location.reload();
}