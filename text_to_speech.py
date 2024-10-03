from gtts import gTTS
import pygame
import os

def text_to_speech(text):
    # Convert the text to speech
    tts = gTTS(text)
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    pygame.mixer.music.stop()
    pygame.mixer.quit()


    # Optionally delete the file after playing
    os.remove(audio_file)


