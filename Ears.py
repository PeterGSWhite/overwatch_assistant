#!/usr/bin/env python3

from threading import Thread
from queue import Queue  # Python 3 import
import speech_recognition as sr
from Brain import think, command_bindings

r = sr.Recognizer()
audio_queue = Queue()
keyword_entries = [(k, v[1]) for k,v in command_bindings.items()]

def recognize_worker():
    # this runs in a background thread
    while True:
        audio = audio_queue.get()  # retrieve the next audio processing job from the main thread
        if audio is None: break  # jstop processing if the main thread is done

        # received audio data, now we'll recognize speech using Sphinx
        try:
            heard = r.recognize_sphinx(audio, keyword_entries=keyword_entries)#, language="en-OW")#, grammar="C:/Users/Peter/proj/manticore/asr.gram")
            think(heard)
            # write audio to a WAV file
            # with open(f"heard-{heard}.wav", "wb") as f:
            #     f.write(audio.get_wav_data())
        except sr.UnknownValueError:
            print("Athena could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        audio_queue.task_done()  # mark the audio processing job as completed in the queue

# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with sr.Microphone() as source:
    try:
        while True:  # repeatedly listen for phrases and put ,..]the resulting audio on the au60777bdio processing job queue
            audio_queue.put(r.listen(source))
    except KeyboardInterrupt:  # allow Ctrl + C to shut down the program
        pass

audio_queue.join()  # block until all current audio processing jobs are done
audio_queue.put(None)  # tell the recognize_thread to stop33
recognize_thread.join()  # wait for the recognize_thread to actually stop