# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.playback import play
# play audio
def play_audio(audio_name):
    try:
        song = AudioSegment.from_mp3(audio_name)
        play(song)
    except KeyboardInterrupt as e:
        print(e)
    finally:
        pass

if __name__ == '__main__':
    pass
