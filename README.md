# inspire

Displays a slideshow of auto-generated "inspirational" quote images.

The quotes are usually nonsensical but gramatically correct, and often amusing.

## Intended use

`./inspire.py --interval <seconds>`

Leave this running on a device with a monitor and internet connection.

I tested on a laptop, but it would probably work on a RaspberryPi.

## Dependencies

* feh
* python3
* an internet connection

## Debugging

Every time the script updates the image, it:
1. fetches a new image from inspirobot.me
2. displays it in a new `feh` window
3. kills the old `feh` window

If it fails to fetch an image (e.g. due to a lost internet connection), it just keeps the previous image on screen until it succeeds.

If you see the rest of your desktop briefly show up during a transition, the new window probably took too long to load (so the old window died before the new one was up). In this case, you can modify the script to wait longer before killing the old window.
