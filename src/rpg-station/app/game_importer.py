from tkinter import Tk
from tkinter import filedialog
from . import game_manager
import os

class GameImporter:
    def import_from_picked_dir(self):
        Tk().withdraw()
        home = os.path.expanduser("~")
        directory = filedialog.askdirectory(initialdir=home)
        if directory != ():
            gm = game_manager.GameManager()
            gm.load_from_dir(directory)

    def import_from_picked_file(self):
        Tk().withdraw()
        home = os.path.expanduser("~")
        filename = filedialog.askopenfilename(initialdir=home)
        if filename != ():
            print(filename)
            print("Trying to import " + filename)
            gm = game_manager.GameManager()
            gm.load_from_file(filename)
        else:
            print("Wrong file picked")

    def import_from_file(self, filename):
        if os.path.exists(filename):
            gm = game_manager.GameManager()
            gm.load_from_file(filename)
        else:
            print("Invalid path to file")
