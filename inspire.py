#!/bin/python3

import subprocess as sp
from requests import get
from time import sleep
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(
        description='display an InspiroBot slideshow',
        epilog='Don\'t use very small update intervals (e.g. 1s); '+ 
               'the script requests an image from `inspirobot.me` on every update, '+
               'and I don\'t know how their servers will react.',
    )
    parser.add_argument('--interval', '-i',
        help='image update interval (in seconds)',
        type=int,
        action='store',
        dest='update_interval_seconds',
        default=30,
    )
    return parser.parse_args()

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
    args = parse_args()

    viewer = UrlImageViewer()
    while True:
        im_url = get_url_until_success("https://inspirobot.me/api?generate=true").content.decode("utf-8")
        viewer.update(im_url)
        sleep(args.update_interval_seconds)
