from youtube_dl import YoutubeDL
from functools import partial
import asyncio

class YTDLsource():
	def __init__(self):
		ytdlopts = {
    		'format': 'bestaudio/best',
    		'outtmpl': 'downloads/%(title)s',
    		'restrictfilenames': True,
    		'noplaylist': True,
    		'nocheckcertificate': True,
   			'ignoreerrors': False,
    		'logtostderr': False,
    		'quiet': True,
    		'no_warnings': True,
    		'default_search': 'auto',
    		'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
		}

		self.ytdl = YoutubeDL(ytdlopts)


	async def create_source(self, url):
		to_run = partial(self.ytdl.extract_info, url=url)
		data = await asyncio.get_event_loop().run_in_executor(None, to_run)

		if 'entries' in data:
			data = data['entries'][0]

		print(data['title'].replace(' ', '_'))

		return [self.ytdl.prepare_filename(data), data]