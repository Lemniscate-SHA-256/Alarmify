import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='user-library-read'
        ))

    def authenticate(self):
        self.sp.current_user()

    def get_playlists(self):
        results = self.sp.current_user_playlists()
        playlists = [item['name'] for item in results['items']]
        return playlists

    def play_playlist(self, playlist_name):
        results = self.sp.current_user_playlists()
        for item in results['items']:
            if item['name'] == playlist_name:
                self.sp.start_playback(context_uri=item['uri'])
                break
