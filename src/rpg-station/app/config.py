import os

def init():
    global RPG_ROOT
    RPG_ROOT = os.getcwd().rsplit('/', 2)[0]
    print("Raspberry Pi Gaming Station Root at: " + RPG_ROOT)
