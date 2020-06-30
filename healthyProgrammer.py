# Healthy Programmer
# 9am - 5 pm
# Water - water.mp3 (3.5 litre) -- Drank -- log -- Every 40 min
# Eyes - eyes.mp3 - every 30 min -- EyDone -- log -- Every 30 min
# Exercise - physical.mp3 - evry 45 min -- exDone -- log
# Pygame module to play mp3

from pygame import mixer
from datetime import datetime
from time import time

def play_mp3(file, stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    stoper = stoper.lower()
    while True:
        a = input()
        if a == stoper:
            mixer.music.stop()
            break
def add_logs(message):
    with open("mylogs.txt", "a") as f:
        f.write(f"{message} : {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exersecs = 10
    eyesecs = 20

    while True:
        if time() - init_water > watersecs:
            print("Time to Drink Water !!!\nEnter Done to stop music : ")
            play_mp3("water.mp3", "Done")
            init_water = time()
            add_logs("Drank Water At ")


        if time() - init_eyes > eyesecs:
            print("Time to Relax Your Eyes !!!\nEnter EyDone to stop music : ")
            play_mp3("eyes.mp3", "EyDone")
            init_eyes = time()
            add_logs("Eyes Relaxed ")

        if time() - init_exercise > exersecs:
            print("Time to do Exercise !!!\nEnter ExDone to stop music : ")
            play_mp3("physical.mp3", "ExDone")
            init_exercise = time()
            add_logs("Exercise Done At ")