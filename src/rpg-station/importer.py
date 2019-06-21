from app.game_importer import GameImporter
from app import config
# This file serves as an entrypoint to importer application

def main():
    config.init()
    print("This is the entrypoint to the game importer")
    importer = GameImporter()
    importer.run()

if __name__ == "__main__":
    main()
