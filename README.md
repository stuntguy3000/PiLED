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
### Normal
Considered as the default mode, this has three rainbow/RGB fade effects.

### Police
Three police style strobe light modes to simulate police light bar.

### Single Colour
Picks a primary colour at random and displays it staticly.


### Party
Various strobe and fast changing effects


### TODO: CS:GO GSI Integration
Provides LED effects for CS:GO using inbuilt GSI.


## Activating Modes
Send a GET request to the application on port `1337` with the URL path of `/mode/<name>`.

A HTTP 200 will be returned on success, a HTTP 404 will be returned on failure (mode not being found). 
The mode name is case-insensitive (and converted to uppercase for internal processing).

e.g. `GET http://127.0.0.1:1337/mode/party` will return a HTTP 200 and activate the Party mode.