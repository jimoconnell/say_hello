#!/usr/bin/env python3
import gtts
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("say", help="Speak the provided phrase")
args = parser.parse_args()

mytext = args.say
if not mytext:
  mytext = "You didn't tell me what to say!"
        
tts = gtts.gTTS(mytext, lang='en')
tts.save("/tmp/tmp.mp3")
os.system("omxplayer /tmp/tmp.mp3")
