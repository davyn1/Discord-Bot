# import necessary packages
import lightbulb
import hikari
import json
import spotipy
import webbrowser

username = '67q2z6s64a3y6kn6u6xfi4xmz'
clientID = '89cf0c7b0c784ad2b48969275e12daf9'
clientSecret = '3c0b82b1f1e144adbdf5a0d8ae28ac95'
redirect_uri = 'http://google.com/callback/'

# pass clientID, clientSecret, and redirect_uri, checks if these 3 parameters are valid or not
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
# gets token as proof of authorized access to Spotify
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# token gets authorized
spotifyObject = spotipy.Spotify(auth=token)
# obtains details of user and combines them
user_name = spotifyObject.current_user()
plugin = lightbulb.Plugin('Spotify')


@plugin.command
@lightbulb.command('music', 'Finds and plays a song on Spotify')
@lightbulb.implements(lightbulb.SlashCommand)
async def play_music(ctx):
    # while True:
    await ctx.respond("Welcome to project")
    if ctx.content == 1:
        print('Found')
        # await ctx.respond(print("Welcome to the project, " + user_name['display_name']))
        # await ctx.respond(print("0 - Exit the console"))
        # await ctx.respond(print("1 - Search for a Song"))
        # ctx = input("Enter Your Choice: ")
        # if ctx == 1:
        #     search_song = input("Enter the song name: ")
        #     results = spotifyObject.search(search_song, 1, 0, "track")
        #     songs_dict = results['tracks']
        #     song_items = songs_dict['items']
        #     song = song_items[0]['external_urls']['spotify']
        #     webbrowser.open(song)
        #     print('Song has opened in your browser.')
        # elif ctx == 0:
        #     print("Good Bye, Have a great day!")
        #     break
        # else:
        #     print("Please enter valid user-input.")


def load(bot):
    bot.add_plugin(plugin)
