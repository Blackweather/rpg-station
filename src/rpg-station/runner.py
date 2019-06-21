from app.app import App
from app import config
# This file serves as an entrypoint to the application

def main():
    config.init()
    print("This is the entrypoint to the application")
    app = App()
    app.run()

if __name__ == "__main__":
    main()
