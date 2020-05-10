# PiLED 
A simple Python application to control **WS2812B** NeoPixel LEDs from a **Raspberry Pi**.

PiLED hosts a web server on port `1337` to run specific modes with pre-defined effects.

## Modes
### Normal
Considered as the default mode, this has three rainbow/RGB fade effects.

### Police
Three police style strobe light modes to simulate police light bar.

### Single Colour
Picks a primary colour at random and displays it staticly.


### TODO: Party
Various strobe and fast changing effects


### TODO: CS:GO GSI Integration
Provides LED effects for CS:GO using inbuilt GSI.


## Activating Modes
Send a GET request to the application on port `1337` with the URL path of `/mode/<name>`.

A HTTP 200 will be returned on success, a HTTP 404 will be returned on failure (mode not being found). 
The mode name is case-insensitive (and converted to uppercase for internal processing).

e.g. `GET http://127.0.0.1:1337/mode/party` will return a HTTP 200 and activate the Party mode.