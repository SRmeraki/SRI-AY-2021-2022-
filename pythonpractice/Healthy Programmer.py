  ############################################------------------HEALTHY PROGRAMMER--------------------------################################

#   for a programmer from 9 to 5 pm = OFFICE TIME
#   1. WATER : You have a water.mp3 file. Ensure that the person is intimated using the mp3 file and takes in 3.5 litres within the office time.
#              After the person drinks water, he must print "DRANK" and at that time , a text file should save the log of time when drank last, and then the mp3 should stop
#   2. EYES : "eyes.mp3 file" - In every 30 mins it should ring and intimate about eye-exercise. After that it should print "DONE".
#   3. Physical Activity : "physical.mp3", in every 45 minutes

## you also need to manage any time clashes

############---to use mp3 file use - PYGAME MODULE to play audio ####################

# import pygame
# import datetime
# import datetime
# import pygame
#
# pygame.init()
#
# # costmizable variables
# water = 'water.mp3'
# eyes = 'eyes.mp3'
# physical = 'physical.mp3'
#
# input_name = input("Please input your name:")
#
# print(f"{input_name.capitalize()} welecome to the office")
#
# file = input_name
#
# water_alarm = 1 # minutes
# eyes_alarm = 2 # minutes
# physical_alarm = 3 # minutes
#
#
# # non-costimizable variables
# ex = True
# d = datetime.datetime.now()
# water_timer = d.minute + water_alarm
# eyes_timer = d.minute + eyes_alarm
# physical_timer = d.minute + physical_alarm
#
# _file = open(file,'a')
#
# print(d)
# while ex!= False:
#     new_d = datetime.datetime.now()
#
#     if water_timer >= 60 or eyes_timer >= 60 or physical_timer >= 60:
#         if water_timer >= 60:
#             water_timer = water_timer - 60
#             d = datetime.datetime.now()
#             minute = d.minute
#
#         if eyes_timer >= 60:
#             eyes_timer = eyes_timer - 60
#             d = datetime.datetime.now()
#             minute = d.minute
#
#         if physical_timer >= 60:
#             physical_timer = physical_timer - 60
#             d = datetime.datetime.now()
#             minute = d.minute
#     else:
#         if new_d.minute == physical_timer and new_d.minute == water_timer:
#             print("Drink water and then do physical",new_d)
#
#             pygame.mixer.music.load(water)
#             pygame.mixer.music.play()
#
#             _input4 = input()
#
#             if _input4.lower() == "drank":
#                 _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
#                 pygame.mixer.music.stop()
#
#             pygame.mixer.music.load(physical)
#             pygame.mixer.music.play()
#
#             _input5 = input()
#             if _input5.lower() == "pydone":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
#                 d = datetime.datetime.now()
#                 eyes_timer = d.minute + eyes_alarm
#                 water_timer = d.minute + water_alarm
#                 physical_timer = d.minute + physical_alarm
#
#
#         elif new_d.minute == physical_timer and new_d.minute == eyes_timer:
#             print("First do eyes exercise and then do physical")
#
#             pygame.mixer.music.load(water)
#             pygame.mixer.music.play()
#
#             _input6 = input()
#
#             if _input6.lower() == "eydone":
#                 _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n ")
#                 pygame.mixer.music.stop()
#
#             pygame.mixer.music.load(physical)
#             pygame.mixer.music.play()
#
#             _input7 = input()
#             if _input7.lower() == "pydone":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
#
#                 d = datetime.datetime.now()
#                 eyes_timer = d.minute + eyes_alarm
#                 water_timer = d.minute + water_alarm
#                 physical_timer = d.minute + physical_alarm
#
#
#
#         elif new_d.minute == water_timer and new_d.minute == eyes_timer:
#             print("Drink water and then do eyes exercise")
#
#             pygame.mixer.music.load(water)
#             pygame.mixer.music.play()
#
#             _input8 = input()
#
#             if _input8.lower() == "eydone":
#                 _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
#                 pygame.mixer.music.stop()
#
#             pygame.mixer.music.load(physical)
#             pygame.mixer.music.play()
#
#             _input9 = input()
#             if _input9.lower() == "drank":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Drank Water at {datetime.datetime.now()} \n \n ")
#                 d = datetime.datetime.now()
#                 eyes_timer = d.minute + eyes_alarm
#                 water_timer = d.minute + water_alarm
#                 physical_timer = d.minute + physical_alarm
#
#         elif new_d.minute == water_timer:
#             print("Please drank water",new_d)
#             pygame.mixer.music.load(water)
#             pygame.mixer.music.play()
#
#             _input = input()
#
#             if _input.lower() == "drank":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
#                 water_timer = d.minute + water_alarm
#
#         elif new_d.minute == eyes_timer:
#             print("Please do eyes exercise",new_d)
#             pygame.mixer.music.load(eyes)
#             pygame.mixer.music.play()
#
#             _input2 = input()
#
#             if _input2.lower() == "eydone":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
#                 eyes_timer = d.minute + eyes_alarm
#
#         elif new_d.minute == physical_timer:
#             print("Please do physical exercise",new_d)
#             pygame.mixer.music.load(physical)
#             pygame.mixer.music.play()
#
#             _input3 = input()
#
#             if _input3.lower() == "pydone":
#                 pygame.mixer.music.stop()
#                 _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
#                 d = datetime.datetime.now()
#                 eyes_timer = d.minute + eyes_alarm
#                 water_timer = d.minute + water_alarm
#                 physical_timer = d.minute + physical_alarm
#
#
#
# _file.close()


###################################################################################
###################### COMPACT METHOD

from pygame import mixer
from datetime import datetime
from time import time

def music_on_loop(file,stopper):
    # mixer.init()    # here init is a function and not constructor inside mixer
    # mixer.music.load(file)
    # mixer.music.play()
    print("playing.....")
    while True:  # this while true is given because we want the music to play at a particular time and stop at a particular time
        a= input()
        if a==stopper:
            print('Stopped')
            # mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt",'a') as f:
        f.write(f'{msg}{datetime.now()}\n')

if __name__=='__main__':
    init_water = time()  #so init_water has some value stored of time ie, now, so as the time keeps increasing , we can figure out the total seconds passed by doing time- init_water
    init_eyes = time()
    init_exercise = time()

    watersecs = 20 #seconds
    eyesecs = 8  #secs
    exersecs = 15 #secs

    while True:
        if time() - init_water>watersecs:
            print('Water Drinking Time!!! Type "drank" to stop the alarm' )
            music_on_loop('water.mp3','drank')
            init_water = time() # here we are updating the init_water time for the next 40 mins
            log_now('Water Drinking Time')

        elif time() - init_eyes>eyesecs:
            print('Eye Exercise Time!!! Type "eye" to stop the alarm ')
            music_on_loop('eye.mp3','eye')
            init_eyes = time()
            log_now('Eye Exercise Time')

        elif time() - init_exercise>exersecs:
            print('Exercise Time!!! Type "exer" to stop the alarm ')
            music_on_loop('exer.mp3','exer')
            init_exercise = time()
            log_now('Exercise Time')

        if input("enter 'exit' to quit program, or 'NO' to continue")=='exit':
            break













