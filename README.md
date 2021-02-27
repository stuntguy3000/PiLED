# PiLED 
A simple Python application to control **WS2812B** NeoPixel LEDs from a **Raspberry Pi**.

PiLED hosts a web server on port `1337` to run specific modes with pre-defined effects.


## Setup
1. Copy/git clone the repository to a folder
2. Make a virtual environment 
3. Enter the virtual environment
4. Install the requirements 
5. Exit the virtual environment 
6. Run the application! 

```
cd /home/pi/PiLED
python3 -m venv venv
source venv/bin/activate
pip3 install --default-timeout=100 -r requirements.txt
deactivate
sudo /home/pi/PiLED/venv/bin/python3 /home/pi/PiLED/PiLED.py
```


## Modes
### Blackout
Used to blackout (turn off) the entire LED strip, over 60 seconds.

### Normal
Considered the "Normal" mode, contains multiple slow speed and low impact effects.

### Party
Contains a collection of strobes and fast moving effects and sequences to send those bangers home.

### Police
Various effects using blue/red/white coloured strobes to emulate Police/EMS light bar sequences.

### SingleFlash
Used to strobe a single colour for a very short amount of time, like a 'tap' button.

### SlowFade
Contains a collection of slow fade in and slow fade out effects: Note, these are triggered by `SlowFadeIn` and by `SlowFadeOut` as required.

### Fire
Emulates a fireplace (vertically). Added by [@bitbrain-za](https://github.com/bitbrain-za/PiLED).


## Activating Modes
Send a GET request to the application on port `1337` with the URL path of `/mode/<name>`.

A HTTP 200 will be returned on success, a HTTP 404 will be returned on failure (mode not being found). 
The mode name is case-insensitive (and converted to uppercase for internal processing).

e.g. `GET http://127.0.0.1:1337/mode/party` will return a HTTP 200 and activate the Party mode.