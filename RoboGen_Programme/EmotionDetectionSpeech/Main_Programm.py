# coding=utf-8

import sys
import Various_Functions
import Processing_Audio
import os

while True:

    sentence = Processing_Audio.getAudioToText()
    sentence = Various_Functions.normalize(sentence)

    if sentence.strip() == "aus" or sentence.strip() == "programm beenden":
        os.system("mpg321 abschied.mp3")
        sys.exit(0)

    else:
        # Funktion für Parsen von Satz
        emotion = Various_Functions.getEmotion(sentence)

        # Funktion für Negierung
        emotion = Various_Functions.checkNegation(sentence, emotion)

        # Funktionen für Weitergabe von Emotion
        print(emotion)
        Various_Functions.talkEmotionToMe(emotion)