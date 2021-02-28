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

from Effects.Util.EffectUtil import *
from Handlers.LEDHandler import LED_COUNT
import time
import random


def run(strip):
    while True:
        # Red Half
        blackout(strip, False)
        for i in range(0, LED_COUNT):
            strip[i] = (0, 255, 0)

        # Update strip
        strip.show()
        # Sleep and add offset
        time.sleep(0.5)

        # Blue Half
        blackout(strip, False)
        for i in range(0, LED_COUNT):
            strip[i] = (100, 0, 255)

        # Update strip
        strip.show()
        # Sleep and add offset
        time.sleep(0.5)
