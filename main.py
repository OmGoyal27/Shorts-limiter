from server import run
import threading
import time
import pyautogui as pg

LIMIT = 180         # Enter the timing in seconds

class TimerThread(threading.Thread):
    def __init__(self, variable):
        super().__init__()
        self.variable = variable
        self.finished = threading.Event()

    def run(self):
        global urll
        if self.variable == "https://www.youtube.com/shorts/":
            time.sleep(180)
            if urll.startswith("https://www.youtube.com/shorts/"):
                print("Watchin boi")
                pg.hotkey("ctrl", "w")

def start_timer(variable):
    timer_thread = TimerThread(variable)
    timer_thread.start()
    return timer_thread

urll = ""
previous_url = ""
def changed(url):
    global urll
    global previous_url
    urll = url
    print(f"Main: {url}")
    print(url)
    shorts = "https://www.youtube.com/shorts/"
    if url.startswith(shorts) and not previous_url.startswith(shorts):
        print("Watching shorts!")
        timer = start_timer(shorts)
    else:
        previous_url = url

if __name__ == '__main__':
    try:
        run()
        
    except KeyboardInterrupt:
        pass