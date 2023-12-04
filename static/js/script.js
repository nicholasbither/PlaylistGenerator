document.addEventListener('DOMContentLoaded', function() {
    var button = document.querySelector('.button');

    button.addEventListener('click', function() {
        alert('Button clicked!');
    });
});

document.querySelectorAll('.mood-button').forEach(button => {
    button.addEventListener('click', function() {
        const moodInput = document.createElement('input');
        moodInput.type = 'hidden';
        moodInput.name = 'mood';
        moodInput.value = this.textContent;
        document.querySelector('form').appendChild(moodInput);

        const relatedArtistsInput = document.getElementById('related-artists');
        relatedArtistsInput.name = 'related-artists';
    });
});