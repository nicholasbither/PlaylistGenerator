# Moodify

## Overview
Moodify is a web application that allows users to create personalized Spotify playlists based on their music preferences and current mood. Users can input criteria such as genre, mood, and artists, and PlaylistGenerator will dynamically generate a specific playlist through interaction with the Spotify API. This project aims to provide an easy and enjoyable experience for music enthusiasts to discover new tracks and collections of tracks with ease.

## Proposed Features
1. **User Input Interface:**
   - Allow users to input preferences, including genre, mood, and preferred artists.
    - Input interface will either be implemented as a web app or by allowing the user to generate a playlist through CLI.

2. **Spotify Playlist Generation:**
   - Implement logic to interpret user preferences and generate a playlist using the Spotify API.

3. **Authentication System:**
   - Set up user authentication securely to enable playlist creation on behalf of the user for their Spotify account.

4. **Intuitive UI/UX Design:**
   - Design an intuitive and user-friendly interface for a smooth user experience.

5. **Testing Framework:**
   - Develop a testing framework to ensure the reliability of backend functions and Spotify API interactions.

6. **Documentation:**
   - Provide comprehensive documentation on how users can utilize the web app and setup instructions for potential developers.

7. **Deployment:**
   - Deploy the web app on a hosting service such as Heroku, AWS, etc. OR
   - Deploy package that can be used to generate playlists using CLI.

## Stakeholders and Intended Users
Moodify is designed for people who enjoy music, who want to discover new tracks tailored to their specific preferences at that given time. Intended users include individuals seeking a personalized and dynamic music discovery experience. No specific background or prerequisites are required, making Moodify accessible to a wide range of users. Stakeholders for this project include both end-users seeking to create playlists, and the developer, who will benefit from a streamlined music discovery tool. Stakeholders could also include the company Spotify itself, as well as users on spotify who create playlists for other people.




## Prerequisites and installation instructions
Required installation: Flask, spotipy, requests. 
pip3 install Flask
pip3 install spotipy
pip3 install requests

## Instructions to run
This web app currently only works locally.
Navigate to the project directory.
To start the server locally, use the command `python3 testapp.py` in your terminal. The application will then be accessible at http://localhost
The user should be immediately prompted with a Spotify login page and is prompted to agree to the permission scope requested by the webapp. 
After agreeing, the user should be redirected to the landing page where there is a UI with different buttons. There should be buttons and selectors associated with playlist generation on the left, and a button to retrieve the user's top 50 saved tracks on the right. 
Currently, the generate_playlist method is broken and will not run.
After clicking the "get top 50 saved tracks" button, the user should be redirected to a page listing all their top saved songs. 


## Proposed future directions
Unfortunately, the method for generate_playlist was not working in time for this deadline. While the user can retrieve their top songs, I'm still working to correct the functionality of the playlist generation. 
Additionally, I did not have time to make the frontend UI look better. I think it would provide a better user experience if the UI was more well organized and aesthetic. Another feature I want to implement is the ability for the user to search songs and artists, get recommended tracks based on a given song (in addition to mood, genre, and artists which I had hoped to have work properly), and displaying the album cover of each song that is displayed on my webapp. 