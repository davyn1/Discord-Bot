# import necessary packages
import hikari
import lightbulb
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import id

plugin = lightbulb.Plugin('Example')
# Spotify API authentication using a token
sp_oauth = SpotifyOAuth(client_id=id.spotify_id,
                        client_secret=id.client_secret,
                        redirect_uri='https://www.google.com/callback/',
                        scope='user-read-playback-state user-modify-playback-state')

token_info = sp_oauth.get_access_token()
if sp_oauth.is_token_expired(token_info):
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
sp = spotipy.Spotify(auth=token_info['access_token'])


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)


@plugin.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@plugin.command
@lightbulb.command('music', 'Plays Music!')
@lightbulb.implements(lightbulb.SlashCommand)
async def music_callback(ctx, track_name: str):
    try:
        results = sp.search(q=track_name, type='track')
        tracks = results['tracks']['items']
        if len(tracks) > 0:
            track = tracks[0]
            response = f"I found the track '{track['name']}' by '{track['artists'][0]['name']}'"
            await ctx.channel.send(response)
        else:
            response = "I couldn't find any tracks with that name."
            await ctx.channel.send(response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        await ctx.channel.send(f"An error occurred: {str(e)}")


def load(bot):
    bot.add_plugin(plugin)
