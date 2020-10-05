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

def run(strip, cooling = 55, sparking = 80, delay = 0.02):
    heat = [0]*LED_COUNT
    cooldown = 0
    
    while True:
        for i in range(0, LED_COUNT):
            cooldown = random.randint(0, round(((cooling * 10) / LED_COUNT) + 20))
            if cooldown > heat[i]:
                heat[i] = 0
            else:
                heat[i] = heat[i] - cooldown

        for i in range(LED_COUNT - 1, 3, -1):
            heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) / 3

        if random.randint(0, 255) < sparking:
            y = random.randint(0, 7)
            heat[y] = heat[y] + random.randint(160, 255)

        for i in range(0, LED_COUNT):
            t192 = round((heat[i]/255.0)*191)

            heatramp = t192 & 0x3F
            heatramp <<= 2
        
            if( t192 > 0x80):
                strip[i] = (255, 255, heatramp)
            elif( t192 > 0x40 ):
                strip[i] = (255, heatramp, 0)
            else:
                strip[i] = (heatramp, 0, 0)

        strip.show()
        time.sleep(delay)
    