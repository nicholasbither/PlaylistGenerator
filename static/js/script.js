

$(document).ready(function() {
    $("#playlist-form").on("submit", function(event) {
       event.preventDefault(); // This line prevents the form from being submitted
   
       // Clear the form fields
       $("#playlist-title").val("");
   
       // Extract the form data
       var mood = document.querySelector('input[name="mood"]').value;
       var artist = document.querySelector('input[name="artist"]').value;
       var genre = document.querySelector('input[name="genre"]').value;
   
       // Generate the playlist on the server side
       fetch('/generate_playlist', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({
               mood: mood,
               artist: artist,
               genre: genre
           })
       })
       .then(response => response.text())
       .then(result => console.log(result))
       .catch(error => console.error('Error:', error));
    });
});


// document.addEventListener('DOMContentLoaded', function() {
//     var button = document.querySelector('.button');

//     button.addEventListener('click', function() {
//         alert('Button clicked!');
//     });
// });


// document.querySelectorAll('.mood-button').forEach(button => {
//     button.addEventListener('click', function() {
//         const moodInput = document.createElement('input');
//         moodInput.type = 'hidden';
//         moodInput.name = 'mood';
//         moodInput.value = this.textContent;
//         document.querySelector('form').appendChild(moodInput);

//         const relatedArtistsInput = document.getElementById('related-artists');
//         relatedArtistsInput.name = 'related-artists';
//     });
// });
// var genreSelect = document.getElementById("genreSelect");
// var selectedGenre = genreSelect.options[genreSelect.selectedIndex].value;


// fetch('/generate_playlist', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         access_token: access_token,
//         user_id: user_id,
//         mood: mood,
//         artist: artist,
//         genre: genre
//     })
// })
// .then(response => response.json())
// .then(data => console.log('Success:', data))
// .catch((error) => console.error('Error:', error));