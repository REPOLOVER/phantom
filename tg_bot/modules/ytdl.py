
from youtube_search import YoutubeSearch
from pytube import YouTube as YT, exceptions
from nicegrill import utils
import os
import json
import logging
import glob
import subprocess


class YouTube:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    async def ytxxx(message):
        args = utils.get_arg(message)
        if not args:
            await message.edit("<i>Enter a search argument first</i>")
            return
        await message.edit("<i>Searching..</i>")
        results = json.loads(YoutubeSearch(args, max_results=10).to_json())
        text = ""
        for i in results["videos"]:
            text += f"<i>◍ {i['title']}</i>\nhttps://www.youtube.com{i['link']}\n\n"
        await message.edit(text)

    async def ytmp3xxx(message, song=None):
        reply = await message.get_reply_message()
        link = utils.get_arg(message) if not song else song
        cmd = f"youtube2mp3 -d {os.getcwd()} -y {link}"
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        for line in process.stdout:
            await message.edit(f"<i>{line.decode()}</i>")
        file = glob.glob("*.mp3")[0]
        await message.edit("<i>Uploading..</i>")
        await message.client.send_file(message.chat_id, file, reply_to=reply.id if reply else None)
        await message.delete()
        os.remove(file)

    async def songxxx(message):
        args = utils.get_arg(message)
        reply = await message.get_reply_message()
        if not args:
            await message.edit("<i>Enter a song name first</i>")
            return
        await message.edit("<i>Searching..</i>")
        results = json.loads(YoutubeSearch(args, max_results=1).to_json())
        if results:
            await message.edit("<i>Downloading</i>")
            link = f"https://www.youtube.com{results['videos'][0]['link']}"
            cmd = f"youtube2mp3 -d {os.getcwd()} -y {link}"
            process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            process.wait()
            await message.edit("<i>Uploading..</i>")
            file = glob.glob("*.mp3")[0]
            await message.client.send_file(message.chat_id, file, reply_to=reply.id if reply else None)
            await message.delete()
            os.remove(file)

    async def ytvidxxx(message):
        url = utils.get_arg(message)
        try:
            await message.edit("<i>Downloading..</i>")
            vid = YT(url).streams.first().download()
            await message.edit("<i>Uploading..</i>")
            await message.client.send_file(message.chat_id, vid, supports_streaming=True)
            await message.delete()
            os.remove(vid)
        except exceptions.RegexMatchError:
            await message.edit("<i>Link might be wrong cuz nothin' found</i>")
