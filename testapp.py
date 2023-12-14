from flask import Flask, render_template, request, redirect, url_for, jsonify, session, json
from flask_bootstrap import Bootstrap
import urllib.parse
#from playlistgenerator import generate_playlist
import unittest
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

app = Flask(__name__, template_folder='templates', static_url_path='')

# Initialize the Flask-Bootstrap extension with app
bootstrap = Bootstrap(app)


app.secret_key = 'f642db8a7a1b4766b77a21cfe5d5a226'
app.config['SESSION_COOKIE_NAME'] = 'my cookie' # correctly configures app with the session cookie name for access token = my cookie, tested this using inspect element 

CLIENT_ID = 'a37a91bdf69e489290e5c30d66f95e69'

CLIENT_SECRET = 'f642db8a7a1b4766b77a21cfe5d5a226'

REDIRECT_URI = 'https://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

TOKEN_INFO = 'token_info'



@app.route('/')
# Route for login/agree to permissions through Spotify
def login():
    """ Login through Spotify and accept permissions 

    Returns:
        Redirects to the authorization url
    """
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/index')
def index():
    """The index route, where my html file renders the frontend UI.

    Returns:
        Renders the template for index.html
    """
    return render_template('index.html')
    

@app.route('/callback')
def callbackPage():
    """ Callback route for authorization, gives the user new token info regarding access tokens.

    Returns:
         Redirects to the landing page (/index)
    """
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect('/index')

@app.route('/getTracks')
def getTracks():
    """ Method to extract the top 50 saved songs from a user's Spotify account

    Returns:
        str: returns a comma seperated string containing the user's top 50 songs in the format Song: song Artist: artist,...
    """
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        redirect("/")
    user_tracks = ""
    sp = spotipy.Spotify(auth=token_info['access_token'])
    saved_tracks = sp.current_user_saved_tracks(limit=50, offset=0)['items']
    for track in saved_tracks:
        user_tracks = user_tracks + '\n' + "Song: " + track['track']['name'] + " Artists: " + str(track['track']['album']['artists'][0]['name']) + ", "
    
    return user_tracks

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    """Method to generate playlists for a user based on their input of mood, genre, and related artists.

    Returns:
        None: The method should create a playlist in the user's Spotify account with the generated tracks added to it.
    """
    try:
        token_info = get_token()
    except:
        # If token info is not valid, redirects the user to login
        print("user not logged in")
        redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
   # Getting user input from the request
    data = request.get_json()
    mood = data['mood']
    artist = data['artist']
    genre = data['genre']
    
    # Create a new playlist to add recommended tracks to:
    user_id = sp.current_user()['id']
    # Creating an empty playlist
    new_playlist = sp.user_playlist_create(user_id, "Recommendations Playlist", True)
    playlist_id = new_playlist['id']
    # Initialize list of uris
    track_uris = []
    # Creating a list of recommended tracks to be added
    tracks = sp.recommendations(seed_artists=artist, seed_genres=genre, limit=20)['items']
    # Loop through the list of recommended tracks, extract their uris, and append to our uri list
    for track in tracks:
        track_uri = track['track']['uri']
        track_uris.append(track_uri)
    # Add the recommended tracks to the playlist, using the track uris as identifiers
    sp.user_playlist_add_tracks(user_id, playlist_id = playlist_id, tracks = track_uris)
    return "Playlist generated successfully!", 200


def get_token():
    """ Method to get an access token from the server. If an access token is expired, will issue a new one using the refresh token

    Returns:
        dict: Returns token_info, a dictionary containing access token, token type, expires_in, refresh token, scope.
    """
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    # Check if access token is expired, use refresh token to issue a new one if expired
    if (is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info
    
    
def create_spotify_oauth():
    """Implementation of OAUTH for the webapp. 
        Uses the information specific to my webapp and the scope needed to create a SpotifyOAuth object.

    """
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=url_for('callbackPage', _external = True),
        show_dialog = True,
        scope = 'user-read-private user-read-email playlist-modify-public user-library-read user-top-read')
    


def test_getTracks():
    # Tests getting top 50 tracks 
    result = getTracks(session['access_token'])
    assert isinstance(result, str)
    assert 'Song: ' in result
    assert ' Artists: ' in result
    
if __name__ == '__main__':
    app.run(debug=True)
    test_getTracks()