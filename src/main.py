import sciter

if __name__ == '__main__':
    frame = sciter.Window(ismain=True, uni_theme=True)
    frame.load_file("../front/main.html")
    frame.expand()
    frame.run_app()
