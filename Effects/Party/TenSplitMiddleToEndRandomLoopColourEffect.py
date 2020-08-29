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


def run(strip, delay_ms=50, leds_per_segment=10, loop_count=10, flash_count=5):
    colour = None

    middle_led = int(LED_COUNT / 2)
    start_led = int(middle_led - leds_per_segment / 2)

    for x in range(0, loop_count):
        colour = get_random_colour(colour)

        for y in range(0, flash_count):
            current_start_led = start_led
            led_loop_count = 0

            while current_start_led < LED_COUNT + leds_per_segment:
                # Top half of the strip
                for z in range(current_start_led, current_start_led + leds_per_segment):
                    if 0 <= z < LED_COUNT:
                        strip[z] = colour

                # Bottom half of the strip
                bottom_led_start = int(middle_led - (leds_per_segment * led_loop_count) - leds_per_segment / 2)
                for z in range(bottom_led_start, bottom_led_start + leds_per_segment):
                    if 0 <= z < LED_COUNT:
                        strip[z] = colour

                strip.show()
                time.sleep(delay_ms / 1000.0)
                blackout(strip, False)
                current_start_led += leds_per_segment
                led_loop_count += 1
