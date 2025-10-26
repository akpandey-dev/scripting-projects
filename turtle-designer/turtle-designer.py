import turtle
import time
import keyboard

# setup
turtle.speed(1)
Time = 0

def motion_pattern():
    turtle.forward(90)
    turtle.right(135)
    time.sleep(1)
    turtle.forward(180)
    turtle.right(90)
    time.sleep(1)
    turtle.forward(180)
    turtle.right(135)
    time.sleep(1)
    turtle.forward(90)

# main motion loop
while Time < 4:
    motion_pattern()
    Time += 1

# infinite loop with 'a' to break
while True:
    motion_pattern()
    if keyboard.is_pressed('a'):
        break
