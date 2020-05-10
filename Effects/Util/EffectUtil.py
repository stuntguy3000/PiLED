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

import random


def blackout(strip, apply=True):
    strip.fill((0, 0, 0))

    if apply:
        strip.show()


def wheel(position):
    """Generate rainbow colors across 0-255 positions."""
    if position < 85:
        return position * 3, 255 - position * 3, 0
    elif position < 170:
        position -= 85
        return 255 - position * 3, 0, position * 3
    else:
        position -= 170
        return 0, position * 3, 255 - position * 3


def get_random_colour(*previous_colours_list):
    colours = [(0, 0, 0) for i in range(7)]

    colours[0] = (255, 0, 0)
    colours[1] = (0, 255, 0)
    colours[2] = (0, 0, 255)
    colours[3] = (255, 255, 0)
    colours[4] = (0, 255, 255)
    colours[5] = (255, 0, 255)
    colours[6] = (255, 255, 255)

    # Todo: UGLY AF
    # Someone else can fix it
    if previous_colours_list is not None:
        for previous_colours_list_loop in previous_colours_list:
            if previous_colours_list_loop is not None:
                for colours_loop in colours:
                    if colours_loop[0] is previous_colours_list_loop[0] and colours_loop[1] is previous_colours_list_loop[1] and colours_loop[2] is previous_colours_list_loop[2]:
                        colours.remove(colours_loop)

    random.shuffle(colours)
    return colours[0]
