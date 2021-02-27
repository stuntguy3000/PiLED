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


def run(strip, delay_ms=50, loop_count=10, flash_count=5):
    previous_colour1 = None
    previous_colour2 = None
    previous_colour3 = None

    for loop_count_loop in range(0, loop_count):
        colour1 = get_random_colour(False, previous_colour1, previous_colour2, previous_colour3)
        previous_colour1 = colour1

        colour2 = get_random_colour(False, previous_colour1, previous_colour2, previous_colour3)
        previous_colour2 = colour2

        colour3 = get_random_colour(False, previous_colour1, previous_colour2, previous_colour3)
        previous_colour3 = colour3

        for flash_count_loop in range(0, flash_count):
            for i in range(0, 40):
                strip[i] = colour1

            strip.show()
            time.sleep(delay_ms / 1000.0)

            blackout(strip, True)
            time.sleep(delay_ms / 1000.0)

            for i in range(40, 80):
                strip[i] = colour2

            strip.show()
            time.sleep(delay_ms / 1000.0)

            blackout(strip, True)
            time.sleep(delay_ms / 1000.0)

            for i in range(80, 120):
                strip[i] = colour3

            strip.show()
            time.sleep(delay_ms / 1000.0)

            blackout(strip, True)
            time.sleep(delay_ms / 1000.0)
