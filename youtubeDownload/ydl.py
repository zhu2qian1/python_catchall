from __future__ import unicode_literals
from sys import argv
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([argv[1]])
