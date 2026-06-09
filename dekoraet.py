import webbrowser

def vildator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("404")
    return wrapper

@vildator
def open_url(url):
   webbrowser.open(url)


open_url("https://ya.ru")