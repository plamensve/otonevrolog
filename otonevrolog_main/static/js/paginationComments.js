document.addEventListener('click', function (event) {
    if (event.target.matches('.pagination a')) {
        event.preventDefault();
        const page = event.target.getAttribute('data-page');
        fetch(`/paginate-comments/?page=${page}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('comments-section').innerHTML = data.html;
            });
    }
});

