from gtts import gTTS
import os
import playsound
mytext = "Hello, my name is Hal how are you?"

language = 'en'

myObj = gTTS(text=mytext, lang=language)
filename = 'response.mp3'
myObj.save(filename)

playsound.playsound(filename)