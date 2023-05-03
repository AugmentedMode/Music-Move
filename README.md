# Apple Music to Spotify <br>
 Some simple python 3 scripts to help import your Apple Music playlists into Spotify playlists. <br >
 **Web-app in Progress!** <br>
 
## Usage
### 1. Export Apple Music playlists to XML File <br >
The first step is to select the playlist you want to import over and export it as an XML file. You do this buy selecting File -> Library -> Export Playlist. Save the resulting file as whatever you would like in the same directory as the directory you cloned this repo into. <br>

### 2. Install dependencies <br >
Install spotipy (use **pip3 install spotipy**) <br >

### 3. Configure Spotify developer application and variables
1. Go to https://developer.spotify.com/dashboard/applications.
2. Create an app with any name.
3. Select the app.
4. Select **EDIT SETTINGS**.
5. Under **Redirect URIs**, enter `http://localhost:8888/callback` and select **Add**. Select **SAVE**.
6. Find **Client ID** and copy the value to the `client_id` variable in [spotify_accessor.py](./spotify_accessor.py).
7. Select **SHOW CLIENT SECRET**. Copy the value to the `client_secret` variable in [spotify_accessor.py](./spotify_accessor.py).
8. Go to https://spotify.com > **Profile** > **Account**.
9. Copy the value of **Username** to the `username` variable in [spotify_accessor.py](./spotify_accessor.py).
10. Save the edited file.


### 4. Run the program <br >
Run the program by using the terminal and navigating to the directory you cloned this repo into. Type in **python3 musicMove.py** to start the program. Follow the intended dirctions and BAM! Your Apple Music playlists are now Spotify playlists! <br >

## Current Issues
### Missing Songs <br >
The script I'm using to retrieve the Spotify identifier for an Apple Music song simply compares the title, artist, and or album depending on search results. Some songs don't have the exact same title in both services which results in the script failing to retrieve an identifier for some songs. At this time the program transfers over 90% of the songs most of the time. The songs that do not get transfered over are printed out on the console for you to add them yourself if you wish.





