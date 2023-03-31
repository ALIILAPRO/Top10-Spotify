import requests

# Set up your Spotify API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Get an access token from the Spotify API
response = requests.post('https://accounts.spotify.com/api/token', data={'grant_type': 'client_credentials'}, auth=(client_id, client_secret))
access_token = response.json()['access_token']

# Set up the headers for the HTTP GET request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Send the HTTP GET request to the Spotify API for the top tracks
response = requests.get('https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks?limit=10', headers=headers)
top_tracks = response.json()['items']

# Print out the track names and artists in a nice, formatted table
print('{:<5} {:<35} {}'.format('Rank', 'Track Name', 'Artist(s)'))
print('-'*55)

for i, track in enumerate(top_tracks):
    rank = str(i+1) + '.'
    name = track['track']['name']
    artists = ', '.join([artist['name'] for artist in track['track']['artists']])
    print('{:<5} {:<35} {}'.format(rank, name, artists))
