from gui.window import Window

class App:
    def run(self):
        print("Initialized the application @app class")
        START_SCREEN_OPT = ["Start", "Controls", "Hotkeys"]
        start_screen = Window(title="Raspberry Pi Gaming Station", choices=START_SCREEN_OPT, controls=[""])
        start_screen.display()
