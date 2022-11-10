"""
This is a echo bot.
It echoes any incoming text messages.
"""
import subprocess
import os
import re
import math
import speech_recognition as sr
from gtts import gTTS

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.input_file import InputFile
from pathlib import Path


API_TOKEN = 'TOKEN_INSERT_HERE'
AUDIO_FILE = 'voice.ogg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def substring_after(s, delim):
    return s.partition(delim)[2]


@ dp.message_handler(content_types=types.ContentTypes.VOICE)
async def handle_voice_documents(message: types.Message):
    print(message.voice.file_id)
    result = await bot.get_file(message.voice.file_id)
    await result.download(AUDIO_FILE)

    r = sr.Recognizer()
    subprocess.call('del -y voice.wav', shell=True)
    subprocess.call('ffmpeg -i voice.ogg voice.wav', shell=True)
    with sr.AudioFile('voice.wav') as source:
        audio = r.record(source)  # read the entire audio file
    mytext=""
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        mytext = r.recognize_google(audio, language="ru-RU")
        print("Google Speech Recognition thinks you said " + mytext)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    # await bot.send_voice(voice=filename)
    text=mytext.lower()
    #pos = mytext.find("калькулятор")
    #if (pos != -1):
    #    text = substring_after(mytext, "калькулятор")
    pi=str(round(math.pi,2))
    text = text.replace("число пи", pi)
    text = text.replace("число пи", pi)
    text = text.replace("числа Пи", pi)
    text = text.replace("числа пи", pi)
    text = text.replace("пи", pi)
    text = text.replace(" x ", "*")
    text = text.replace(" х ", "*")
    #text = re.sub('\s+x\s', '*', text)
    #text = re.sub('\s+х\s', '*', text)
    text = text.replace("умножить", "*")
    text = text.replace("разделить", "/")
    text = text.replace("в степени", "**")

    #chars = set('0123456789$+*/ ')
    #if any((c in chars) for c in text):
    #bad_chars = set(text) - set('0123456789$+*/ ') # set(X,Y)
    #if not any(c not in '0123456789$+*/ ' for c in text):

    if not re.search('[^0123456789$+*/ .]', text):
        print('Found expression')
        try:
            ev=eval(text)
            await message.answer(f"Результат: {ev}!")
            await bot.send_voice(message.chat.id, tovoice("Наш результат: "+str(ev)), caption="Наш ответ")
            
        except (SyntaxError, NameError) as e:
            await message.answer(f"Вы сказали но я не понял!{mytext}")
    else:
        print('Not Found')
        await message.answer(f"Вы сказали но я не понял!{mytext}")

def tovoice(text):
    tts = gTTS(text,lang="ru")
    tts.save('voice.mp3')
    subprocess.call('del -y voicex.ogg', shell=True)
    subprocess.call('ffmpeg -i voice.mp3 -c:a libopus voicex.ogg', shell=True)
    out_filename="voicex.ogg"
    path = Path("", out_filename)
    voice = InputFile(path)
    return voice
    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_voice(message.chat.id, tovoice("Попробуйте наш голосовой калькулятор"), caption="Наш ответ")
    await message.reply("Попробуйте наш голосовой калькулятор")
    

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)

#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
