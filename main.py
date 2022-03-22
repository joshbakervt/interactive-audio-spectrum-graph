# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
import webbrowser

def main():
    username = 'joshbakervt'
    clientID = '0d50987c4fc84765b643819b08e00225'
    clientSecret = ''
    redirectURI = 'https://www.google.com'

    # Create OAuth Object
    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)

    # Create token
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']

    # Create Spotify Object
    spotifyObject = spotipy.Spotify(auth=token)

    user = spotifyObject.current_user()

    # To print the response in readable format.
    # print(json.dumps(user,sort_keys=True, indent=4))


    # TODO: Display contents in PyQt5 Window from json retrieval

    while True:
        print("Welcome, " + user['display_name'])
        print("0 - Exit")
        print("1 - Search for a Song")
        choice = int(input("Your Choice: "))
        if choice == 1:
            # Logic for search functionality
            # Get the Song Name.
            searchQuery = input("Enter Song Name: ")
            # Search for the Song.
            searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
            # Get required data from JSON response.
            tracks_dict = searchResults['tracks']
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            # Open the Song in Web Browser
            webbrowser.open(song)
            print('Song has opened in your browser.')
        elif choice == 0:
            break
        else:
            print("Enter valid choice.")


        # TODO: Integrate Web Audio API to manipulate and visualize playback

main()
