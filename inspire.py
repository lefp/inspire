#!/bin/python3

import subprocess as sp
from requests import get
from time import sleep

UPDATE_INTERVAL_SECONDS = 30

# tries requests.get(url) over and over till it works
def get_url_until_success(url: str):
    while True:
        try: return get(url)
        except: sleep(10)

class UrlImageViewer:
    proc: sp.Popen = None

    def update(self, url):
        new_proc = sp.Popen([
            "/bin/feh",
            "--fullscreen",
            "--auto-zoom",
            "--image-bg", "black",
            "--hide-pointer",
            url
        ])

        sleep(1) # give new window a second to show up before killing old one
        if self.proc is not None: self.proc.kill()
        self.proc = new_proc

if __name__ == "__main__":
    proc = None

    viewer = UrlImageViewer()
    while True:
        im_url = get_url_until_success("https://inspirobot.me/api?generate=true").content.decode("utf-8")
        viewer.update(im_url)
        sleep(UPDATE_INTERVAL_SECONDS)
