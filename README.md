# Spotify-top-playlist
Atumoation project for creating spotify playlists. Script add top 10 tracks of every given artist to the list.

### Dependencies
```
pip3 install -r requirements.txt
```

### Config file
Replace data in *config.json* with your parameters: 
- spotify user id - get this from your spotify account overview,
- spotify token - get it from: [Token url], one lasts for only one hour, ater that you have to generate new one,  
- artists - list of artists that you want in your playlist.

### Run
```
python3 create.py
```

  [Token url]: <https://developer.spotify.com/console/post-playlists/>
