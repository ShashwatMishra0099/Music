from pyrogram import Client, filters
from pytgcalls import GroupCall
from youtube_search import YoutubeSearch

API_ID = '29597128'
API_HASH = 'feea1340241265662aec5d75678e9573'
BOT_TOKEN = '7150134362:AAE8w3s_05GepcgScZUS-Zn27mR8Bmz8UV0'

app = Client('music_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
group_call = GroupCall(app)

@app.on_message(filters.command('start'))
async def start(client, message):
    await message.reply_text('Welcome to the Music Bot! Send /play followed by the name of the song you want to listen to.')

@app.on_message(filters.command('play'))
async def play(client, message):
    query = ' '.join(message.command[1:])
    results = YoutubeSearch(query, max_results=1).to_dict()
    if results:
        video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"
        await message.reply_text(f'Playing: {video_url}')
        await group_call.start(message.chat.id, video_url)

@app.on_message(filters.command('stop'))
async def stop(client, message):
    await group_call.stop(message.chat.id)

app.run()
