from app.app import App
# This file serves as an entrypoint to the application

def main():
    print("This is the entrypoint to the application")
    app = App()
    app.run()

if __name__ == "__main__":
    main()
