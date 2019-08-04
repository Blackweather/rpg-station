from app.game_importer import GameImporter
from app import config
import sys
# This file serves as an entrypoint to importer application

def main():
    config.init()
    print("This is the entrypoint to the game importer")
    importer = GameImporter()
    if len(sys.argv) == 1:
        importer.import_from_picked_dir()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-f":
            importer.import_from_picked_file()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f":
            importer.import_from_file(sys.argv[2])

if __name__ == "__main__":
    main()
