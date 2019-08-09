from tkinter import Tk
from tkinter import filedialog
from . import game_manager

class GameImporter:
    def import_from_picked_dir(self):
        Tk().withdraw()
        directory = filedialog.askdirectory()
        if directory != ():
            gm = game_manager.GameManager()
            gm.load_from_dir(directory)

    def import_from_picked_file(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename()
        if filename != None:
            gm = game_manager.GameManager()
            gm.load_from_file(filename)

    def import_from_file(self, filename):
        pass
