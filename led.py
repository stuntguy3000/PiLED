#!/usr/bin/env python3

#  The MIT License
#
#  Copyright (c) 2020 Luke Anderson (stuntguy3000)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import time
import random
import argparse
import multiprocessing
import SocketServer
import SimpleHTTPServer
import os

from neopixel import *

LED_THREAD = None

LED_COUNT = 120
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


# Helper Functions
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def blackout(strip, applyStrip=True):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))

    if applyStrip:
        strip.show()


def allWhite(strip, wait_ms=30, loopCount=40):
    blackout(strip, False)
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(255, 255, 255))
    strip.show()


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def getRandomListColour(*previousColors):
    colours = [Color(0, 0, 0) for i in range(7)]

    colours[0] = Color(255, 0, 0)
    colours[1] = Color(0, 255, 0)
    colours[2] = Color(0, 0, 255)
    colours[3] = Color(255, 255, 0)
    colours[4] = Color(0, 255, 255)
    colours[5] = Color(255, 0, 255)
    colours[6] = Color(255, 255, 255)

    if previousColors != None:
        for loopColour in previousColors:
            if (loopColour in colours):
                colours.remove(loopColour)

    random.shuffle(colours)
    return colours[0]


# Generic
def rainbow(strip, wait_ms=20, iterations=5, loopIncrementModifier=1, isStrobe=False):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(0, 256 * iterations, loopIncrementModifier):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)

        if isStrobe:
            blackout(strip, True)
            time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5, loopIncrementModifier=1, isStrobe=False):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(0, 256 * iterations, loopIncrementModifier):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)

        if isStrobe:
            blackout(strip, True)
            time.sleep(wait_ms / 1000.0)


def allRainbowCycle(strip, wait_ms=20, loopCount=5, loopIncrementModifier=1, isStrobe=False):
    for loopCountLoop in range(0, loopCount):
        for x in range(0, 255, loopIncrementModifier):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel(x))

            strip.show()
            time.sleep(wait_ms / 1000.0)

        if isStrobe:
            blackout(strip, True)
            time.sleep(wait_ms / 1000.0)


# Party
def splitDualRandom(strip, wait_ms, loopCount, flashCount, isStrobe):
    if (isStrobe == False):
        wait_ms = wait_ms * 2

    previousColor1 = None
    previousColor2 = None
    for loopCountLoop in range(0, loopCount):
        colour1 = getRandomListColour(previousColor1, previousColor2)
        previousColor1 = colour1

        colour2 = getRandomListColour(previousColor2, previousColor1)
        previousColor2 = colour2

        for flashCountLoop in range(0, flashCount):
            for i in range(59, 119):
                strip.setPixelColor(i, colour1)

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)
            else:
                blackout(strip, False)

            for i in range(0, 59):
                strip.setPixelColor(i, colour2)

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)
            else:
                blackout(strip, False)


def triSplitRandom(strip, wait_ms, loopCount, flashCount):
    previousColor1 = None
    previousColor2 = None
    previousColor3 = None
    for loopCountLoop in range(0, loopCount):
        colour1 = getRandomListColour(previousColor1, previousColor2, previousColor3)
        previousColor1 = colour1

        colour2 = getRandomListColour(previousColor2, previousColor1, previousColor3)
        previousColor2 = colour2

        colour3 = getRandomListColour(previousColor2, previousColor1, previousColor3)
        previousColor3 = colour3

        for flashCountLoop in range(0, flashCount):
            for i in range(0, 39):
                strip.setPixelColor(i, colour1)

            strip.show()
            time.sleep(wait_ms / 1000.0)
            blackout(strip, True)

            for i in range(39, 79):
                strip.setPixelColor(i, colour2)

            strip.show()
            time.sleep(wait_ms / 1000.0)
            blackout(strip, True)

            for i in range(80, 119):
                strip.setPixelColor(i, colour3)

            strip.show()
            time.sleep(wait_ms / 1000.0)
            blackout(strip, True)


def alternatingRandom(strip, wait_ms, loopCount, flashCount, isStrobe):
    if (isStrobe == False):
        wait_ms = wait_ms * 2

    previousColor = None
    for loopCountLoop in range(0, loopCount):
        colour = getRandomListColour(previousColor)
        previousColor = colour

        for flashCountLoop in range(0, flashCount):
            for i in range(0, strip.numPixels()):
                if i % 2 == 0:
                    strip.setPixelColor(i, colour)
                else:
                    strip.setPixelColor(i, Color(0, 0, 0))

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)

            for i in range(0, strip.numPixels()):
                if i % 2 == 1:
                    strip.setPixelColor(i, colour)
                else:
                    strip.setPixelColor(i, Color(0, 0, 0))

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)


def allRandom(strip, wait_ms, loopCount, flashCount, isStrobe):
    if (isStrobe == False):
        wait_ms = wait_ms * 2

    previousColor = None

    for loopCountLoop in range(0, loopCount):
        colour = getRandomListColour(previousColor)
        previousColor = colour

        for flashCountLoop in range(0, flashCount):
            for i in range(0, strip.numPixels()):
                strip.setPixelColor(i, colour)

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms * 2 / 1000.0)


def allPixelRandom(strip, wait_ms, loopCount, isStrobe):
    if (isStrobe == False):
        wait_ms = wait_ms * 2

    previousColor = None

    for flashCountLoop in range(0, loopCount):
        for i in range(0, strip.numPixels()):
            colour = getRandomListColour(previousColor)
            previousColor = colour
            strip.setPixelColor(i, colour)

        strip.show()
        time.sleep(wait_ms / 1000.0)

        if isStrobe:
            blackout(strip, True)
            time.sleep(wait_ms * 2 / 1000.0)


def dualAlternatingRandom(strip, wait_ms, loopCount, flashCount, isStrobe):
    if (isStrobe == False):
        wait_ms = wait_ms * 2

    previousColor1 = None
    previousColor2 = None
    for loopCountLoop in range(0, loopCount):
        colour1 = getRandomListColour(previousColor1, previousColor2)
        previousColor1 = colour1

        colour2 = getRandomListColour(previousColor2, previousColor1)
        previousColor2 = colour2

        for flashCountLoop in range(0, flashCount):
            for i in range(0, strip.numPixels()):
                if i % 2 == 0:
                    strip.setPixelColor(i, colour1)
                else:
                    strip.setPixelColor(i, Color(0, 0, 0))

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)

            for i in range(0, strip.numPixels()):
                if i % 2 == 1:
                    strip.setPixelColor(i, colour2)
                else:
                    strip.setPixelColor(i, Color(0, 0, 0))

            strip.show()
            time.sleep(wait_ms / 1000.0)

            if isStrobe:
                blackout(strip, True)
                time.sleep(wait_ms / 1000.0)


# 1 = Left to Right 	2 = Right to Left	3 = Middle to Edge	4 = Edge to Middle
def directionalRandom(strip, wait_ms, loopCount, doBlackout, direction, ignoreColour=None, randomColor=False):
    previousColor = ignoreColour
    for loopCountLoop in range(0, loopCount):
        color = getRandomListColour(previousColor)
        previousColor = color

        if (doBlackout):
            blackout(strip)

        # 1 = Left to Right
        if (direction == 1):
            for i in range(0, strip.numPixels(), 1):
                if (randomColor):
                    color = getRandomListColour(color)

                strip.setPixelColor(i, color)

                strip.show()
                time.sleep(wait_ms / 1000.0)

        # 2 = Right to Left
        if (direction == 2):
            for i in range(strip.numPixels(), 0, -1):
                if (randomColor):
                    color = getRandomListColour(color)

                strip.setPixelColor(i, color)

                strip.show()
                time.sleep(wait_ms / 1000.0)

        # 3 = Middle to Edge
        if (direction == 3):
            middle = int(round(strip.numPixels() / 2))
            foundEdge = False
            increment = 0

            while (foundEdge == False):
                if (randomColor):
                    color = getRandomListColour(color)

                strip.setPixelColor(middle + increment, color)
                strip.setPixelColor(middle - increment, color)
                increment += 1

                strip.show()
                time.sleep(wait_ms / 1000.0)

                if ((increment + middle) > strip.numPixels()):
                    foundEdge = True

        # 4 = Edge to Middle
        if (direction == 4):
            middle = int(round(strip.numPixels() / 2))

            for i in range(0, middle + 1):
                if (randomColor):
                    color = getRandomListColour(color)

                strip.setPixelColor(i, color)
                strip.setPixelColor(strip.numPixels() - i, color)

                strip.show()
                time.sleep(wait_ms / 1000.0)

    return previousColor


def singleColourRotation(strip, wait_ms, loopCount=10):
    previousColor = ignoreColour


# for loopCountLoop in range(0, loopCount):
# TODO


# Light Modes
def modeParty():
    while (True):
        randomNumber = random.randint(0, 10)

        if randomNumber == 1:
            splitDualRandom(strip, 50, 30, 5, bool(random.getrandbits(1)))

        if randomNumber == 2:
            alternatingRandom(strip, 50, 100, 1, bool(random.getrandbits(1)))

        if randomNumber == 3:
            dualAlternatingRandom(strip, 50, 15, 5, bool(random.getrandbits(1)))

        if randomNumber == 4:
            allRandom(strip, 50, 100, 1, bool(random.getrandbits(1)))

        if randomNumber == 5:
            rainbowCycle(strip, 50, 15, 60, True)

        if randomNumber == 6:
            rainbow(strip, 50, 15, 60, True)

        if randomNumber == 7:
            ignoreColour = None
            for i in range(0, 15):
                ignoreColour = directionalRandom(strip, 0, 1, True, 1, ignoreColour, bool(random.getrandbits(1)))
                ignoreColour = directionalRandom(strip, 0, 1, True, 2, ignoreColour, bool(random.getrandbits(1)))

        if randomNumber == 8:
            allPixelRandom(strip, 25, 180, True)

        if randomNumber == 9:
            allRandom(strip, 50, 10, 10, True)

        if randomNumber == 10:
            triSplitRandom(strip, 50, 30, 5)


def modePolice():
    while (True):
        """ Animation One - Alternating Pattern """
        for y in range(0, 4):
            for z in range(0, 10):
                for i in range(0, strip.numPixels()):
                    if i % 2 == 0:
                        strip.setPixelColor(i, Color(0, 0, 255))
                    else:
                        strip.setPixelColor(i, Color(0, 0, 0))
                strip.show()
                time.sleep(0.05)

                blackout(strip, True)
                time.sleep(0.05)

            for z in range(0, 10):
                for i in range(0, strip.numPixels()):
                    if i % 2 != 0:
                        strip.setPixelColor(i, Color(0, 255, 0))
                    else:
                        strip.setPixelColor(i, Color(0, 0, 0))

                strip.show()
                time.sleep(0.05)

                blackout(strip, True)
                time.sleep(0.05)

        """ Animation Two - Split Red, White, Blue """
        for x in range(0, 4):
            for y in range(0, 12):
                for i in range(0, 39):
                    strip.setPixelColor(i, Color(0, 0, 255))
                for i in range(39, 79):
                    strip.setPixelColor(i, Color(0, 0, 0))
                for i in range(79, 119):
                    strip.setPixelColor(i, Color(0, 255, 0))

                strip.show()
                time.sleep(0.05)

                blackout(strip, False)
                for i in range(39, 79):
                    strip.setPixelColor(i, Color(200, 200, 200))

                strip.show()
                time.sleep(0.04)

                blackout(strip, True)
                time.sleep(0.01)

            for y in range(0, 12):
                for i in range(0, 39):
                    strip.setPixelColor(i, Color(0, 255, 0))
                for i in range(39, 79):
                    strip.setPixelColor(i, Color(0, 0, 0))
                for i in range(79, 119):
                    strip.setPixelColor(i, Color(0, 0, 255))

                strip.show()
                time.sleep(0.05)

                blackout(strip, False)
                for i in range(39, 79):
                    strip.setPixelColor(i, Color(200, 200, 200))

                strip.show()
                time.sleep(0.04)

                blackout(strip, False)

                strip.show()
                time.sleep(0.01)

        """ Animation Three - Half/Half Alternating Strobe Red, Blue """
        for y in range(0, 4):
            for x in range(0, 10):
                for i in range(0, 59):
                    strip.setPixelColor(i, Color(0, 0, 255))
                for i in range(59, 119):
                    strip.setPixelColor(i, Color(0, 0, 0))

                strip.show()
                time.sleep(0.05)

                for i in range(0, 59):
                    strip.setPixelColor(i, Color(0, 0, 0))
                for i in range(59, 119):
                    strip.setPixelColor(i, Color(0, 255, 0))

                strip.show()
                time.sleep(0.05)

            for x in range(0, 10):
                for i in range(0, 59):
                    strip.setPixelColor(i, Color(0, 255, 0))
                for i in range(59, 119):
                    strip.setPixelColor(i, Color(0, 0, 0))

                strip.show()
                time.sleep(0.05)

                for i in range(0, 59):
                    strip.setPixelColor(i, Color(0, 0, 0))

                for i in range(59, 119):
                    strip.setPixelColor(i, Color(0, 0, 255))

                strip.show()
                time.sleep(0.05)


def modeNormal():
    while (True):
        randomNumber = random.randint(1, 4)

        if randomNumber == 1:
            rainbowCycle(strip)

        if randomNumber == 2:
            allRainbowCycle(strip)

        if randomNumber == 3:
            rainbow(strip)

        if randomNumber == 4:
            ignoreColour = None
            for i in range(0, 15):
                ignoreColour = directionalRandom(strip, 25, 1, False, 4, ignoreColour)
                ignoreColour = directionalRandom(strip, 25, 1, False, 3, ignoreColour)

        if randomNumber == 5:
            singleColourRotation(strip)


def modeWhite():
    while (True):
        allWhite(strip)


def modeStrikers():
    blackout(strip, False)
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(75, 0, 255))
    strip.show()


def modeRed():
    blackout(strip, False)
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 255, 0))
    strip.show()


# Control Functions
def cancelCurrentThread():
    if (LED_THREAD != None):
        LED_THREAD.terminate()


# Web Server
class LEDControlHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        global LED_THREAD
        if self.path == "/control/party":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modeParty)
        elif self.path == "/control/normal":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modeNormal)
        elif self.path == "/control/police":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modePolice)
        elif self.path == "/control/white":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modeWhite)
        elif self.path == "/control/strikers":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modeStrikers)
        elif self.path == "/control/red":
            cancelCurrentThread()
            LED_THREAD = multiprocessing.Process(target=modeRed)
        elif self.path == "/control/shutdown":
            cancelCurrentThread()
            blackout(strip, True)
            os.system("sudo shutdown -h now")
        else:
            return

        LED_THREAD.start()


# Run the Program
if __name__ == '__main__':
    # Initlalize Strip
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    # Start with normal modeNormal
    LED_THREAD = multiprocessing.Process(target=modeNormal)
    LED_THREAD.start()

    # Run Web Server
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.ThreadingTCPServer(('', 1234), LEDControlHandler)
    server.serve_forever()
