from tkinter import Tk
from tkinter.filedialog import askdirectory
from . import game_manager

class GameImporter:
    def run(self):
        Tk().withdraw()
        directory = askdirectory()
        if directory != ():
            gm = game_manager.GameManager()
            gm.load_from_dir(directory)
