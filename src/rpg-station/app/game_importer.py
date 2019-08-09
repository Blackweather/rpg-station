from tkinter import Tk
from tkinter import filedialog
from . import game_manager
import os

class GameImporter:
    def import_from_picked_dir(self):
        Tk().withdraw()
        directory = filedialog.askdirectory()
        if directory != ():
            gm = game_manager.GameManager()
            gm.load_from_dir(directory)

    def import_from_picked_file(self):
        #TODO: fix logs here?
        Tk().withdraw()
        filename = filedialog.askopenfilename()
        if filename != None:
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
