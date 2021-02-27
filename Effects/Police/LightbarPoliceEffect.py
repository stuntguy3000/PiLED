#  The MIT License
#
#  Copyright (c) 2021 Luke Anderson (stuntguy3000)
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


def run(strip, loop_count=4, flash_count=10):
    for x in range(0, loop_count):
        for y in range(0, flash_count):
            for i in range(0, 39):
                strip[i] = (0, 0, 255)
            for i in range(39, 79):
                strip[i] = (0, 0, 0)
            for i in range(79, 119):
                strip[i] = (0, 255, 0)

            strip.show()
            time.sleep(0.05)

            blackout(strip, False)
            for i in range(39, 79):
                strip[i] = (255, 255, 255)

            strip.show()
            time.sleep(0.04)

            blackout(strip, True)
            time.sleep(0.01)

        for y in range(0, flash_count):
            for i in range(0, 39):
                strip[i] = (0, 255, 0)
            for i in range(39, 79):
                strip[i] = (0, 0, 0)
            for i in range(79, 119):
                strip[i] = (0, 0, 255)

            strip.show()
            time.sleep(0.05)

            blackout(strip, False)
            for i in range(39, 79):
                strip[i] = (255, 255, 255)

            strip.show()
            time.sleep(0.04)

            blackout(strip, False)

            strip.show()
            time.sleep(0.01)
