# project -- alarm clock
from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        time_left_minutes = time_left // 60
        time_left_seconds = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {time_left_minutes:02d}:{time_left_seconds:02d}")

    playsound("ringtone.mp3")
minutes = int(input("How many minutes do you want to set the alarm for? "))
seconds = int(input("How many seconds do you want to set the alarm for? "))
alarm(minutes * 60 + seconds)