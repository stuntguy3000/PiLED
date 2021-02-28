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


def run(strip, loop_count=4, flash_count=5):
    for x in range(0, loop_count):
        for y in range(0, flash_count):
            for i in range(0, LED_COUNT):
                if i % 2 == 0:
                    strip[i] = (0, 0, 255)
                else:
                    strip[i] = (0, 0, 0)
            strip.show()
            time.sleep(0.05)

            blackout(strip, True)
            time.sleep(0.05)

            for i in range(0, LED_COUNT):
                if i % 2 == 0:
                    strip[i] = (0, 0, 0)
                else:
                    strip[i] = (0, 0, 255)
            strip.show()
            time.sleep(0.05)

            blackout(strip, True)
            time.sleep(0.05)

        for y in range(0, flash_count):
            for i in range(0, LED_COUNT):
                if i % 2 == 0:
                    strip[i] = (0, 255, 0)
                else:
                    strip[i] = (0, 0, 0)
            strip.show()
            time.sleep(0.05)

            blackout(strip, True)
            time.sleep(0.05)

            for i in range(0, LED_COUNT):
                if i % 2 == 0:
                    strip[i] = (0, 0, 0)
                else:
                    strip[i] = (0, 255, 0)
            strip.show()
            time.sleep(0.05)

            blackout(strip, True)
            time.sleep(0.05)
