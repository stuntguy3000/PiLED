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

from Handlers.LEDHandler import LED_COUNT
from Effects.Util.EffectUtil import *

import random


class SegmentOrder:
    RANDOM = 0  # Random Segment Order
    FIRST_TO_LAST = 1  # First Segment to Last Segment
    LAST_TO_FIRST = 2  # Last Segment to First Segment


# Generates a list of indexes which represent the start of segments on a LED script
# For example, splitting a strip of 120 LEDs with segments of length 10
# should return the length of each segment and a list of [10, 0, 10, 20, 30, 40, 50, 70, 80, 90, 100, 110]
def get_segments(segment_count, segment_order=SegmentOrder.FIRST_TO_LAST, skip_first_segment=False,
                 skip_last_segment=False):
    # Validity check (segment_count must be more than 1 segment and divisible by LED_COUNT)
    if segment_count < 1 or segment_count % LED_COUNT == 0:
        # Return no segments
        return 0, []

    # Generate Segments
    segment_list = []
    length = int(LED_COUNT / segment_count)
    for i in range(0, LED_COUNT, length):
        segment_list.append(i)

    if skip_first_segment is True:
        segment_list.pop(0)

    if skip_last_segment is True:
        segment_list.pop(len(segment_list) - 1)

    # Order segments (FIRST_TO_LAST is the catch all condition)
    if segment_order == SegmentOrder.LAST_TO_FIRST:
        segment_list.sort(reverse=True)
    elif segment_order == SegmentOrder.RANDOM:
        random.shuffle(segment_list)

    return length, segment_list


def display_segments(strip, segment_data, cycle_delay, color=None, random_colour_allow_black=False,
                     blackout_after_delay=0, blackout_before=True):
    """
    Cycles through all segments using defined parameters
    :param strip: the LED strip object
    :param segment_data: the returned data from get_segments
    :param cycle_delay: the time in ms to delay the cycle changes by
    :param color: the colour to use on each cycle. If None, a random colour is chosen (Default None)
    :param random_colour_allow_black: Dictates if a randomly chosen colour can be black.
    :param blackout_after_delay: to blackout the strip after cycle_delay, set this value to a length above 0 (Default 0)
    :param blackout_before: blackouts the strip before cycling (Default True)
    """
    segment_length = segment_data[0]
    segment_indexes = segment_data[1]

    previous_colour = None

    for index in range(0, len(segment_indexes)):
        if blackout_before:
            blackout(strip, False)

        chosen_colour = color

        if chosen_colour is None:
            chosen_colour = get_random_colour(random_colour_allow_black, previous_colour)

        segment_start = segment_indexes[index]
        for ledIndex in range(segment_start, segment_start + segment_length):
            strip[ledIndex] = chosen_colour

        strip.show()
        time.sleep(cycle_delay)

        if blackout_after_delay > 0:
            blackout(strip, True)
            time.sleep(blackout_after_delay)
