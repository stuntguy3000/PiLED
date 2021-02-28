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


def run(strip, delay_ms=20, loop_count=5 * 255, base_modifier_increment=10):
    """ Slowly rotate though a across 5 pixels, repeated across the entire strip """

    base_modifier = 0
    for j in range(0, loop_count):
        base_modifier += base_modifier_increment

        if base_modifier > 255:
            base_modifier = 0

        for start_strip_index in range(0, LED_COUNT, 15):
            for i in range(15):
                if i + start_strip_index < LED_COUNT:
                    position = base_modifier + (17 * i)

                    while position > 255:
                        position = position - 255

                    strip[start_strip_index + i] = wheel(position)

        strip.show()
        time.sleep(delay_ms / 1000.0)
