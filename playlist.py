import requests
import json


class CreatePlaylist:

    def __init__(self):
        self.user_id = None
        self.token = None
        self.artists = None
        self.config_file = 'config.json'
        self.load_config()


    def load_config(self):
        with open(self.config_file, 'r') as file:
            spotify_user_params = json.load(file)
            self.token = spotify_user_params['spotify_token']
            self.user_id = spotify_user_params['spotify_user_id']
            self.artists = spotify_user_params['artists']
            print('Config loaded')


    def create_playlist(self):
        endpoint_url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'
        request_body = json.dumps({
                'name': 'Top of artists',
                'description': 'Top songs of artists. Created with Python',
                'public': False
                })
        create_response = requests.post(url = endpoint_url, 
                                data = request_body, 
                                headers={'Content-Type': 'application/json', 
                                        'Authorization': f'Bearer {self.token}'})

        url = create_response.json()['external_urls']['spotify']
        if create_response.status_code == 201:
            print('Playlist created')

        return create_response.json()['id']


    def get_artists_id(self):
        artists_ids = []
        query = f'https://api.spotify.com/v1/search'
        for artist in self.artists:
            artist_info = requests.get(query,
                headers={ 'authorization': "Bearer " + self.token}, 
                params={ 'q': artist, 'type': 'artist' })
            artists_ids.append(artist_info.json()['artists']['items'][0]['id'])

        return artists_ids


    def get_top_artist_songs(self):
        uris = [] 
        ids = self.get_artists_id()
        for id in ids:   
            query = f'https://api.spotify.com/v1/artists/{id}/top-tracks?country=US'
            top_tracks_response = requests.get(query, 
                    headers={'Content-Type': 'application/json', 
                                'Authorization': f'Bearer {self.token}'})
            json_response = top_tracks_response.json()
            for i,j in enumerate(json_response['tracks']):
                uris.append(j['uri'])

        return uris

    
    def fill_playlist(self):
        playlist_id = self.create_playlist()
        uris = self.get_top_artist_songs()

        endpoint_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        request_body = json.dumps({
              'uris' : uris
                })
        fill_response = requests.post(url = endpoint_url, 
                                data = request_body, 
                                headers={'Content-Type': 'application/json', 
                                            'Authorization': f'Bearer {self.token}'})

        if fill_response.status_code == 201:
            print('Tracks were added to your playlist')
