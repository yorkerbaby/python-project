"""
File: Steeplechase.py
Name:Isaac:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
       if front_is_clear():
        move()
       else:
        jump()

def jump():
    """
    Pre-condition:Karel is on the left,facing East
    Post-condition:
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition:Karel is on the left,facing East
    Post-condition:
    """
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """


    """
    turn_right()
    move()
    turn_right()


def down():
    """


    """
    move()
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
