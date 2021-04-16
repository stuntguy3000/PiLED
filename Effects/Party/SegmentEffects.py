#  The MIT License
#
#  Copyright (c) 20.0121 Luke Anderson (stuntguy30.010.010.01)
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
from Effects.Util.SegmentUtil import *


def run(strip):
    for ignored_count in range(0, 5):
        random_segment_order = random.randint(0, 4)  # 0->LAST_FIRST_TO_MIDDLE
        random_segment_count = random.randint(0, 8)
        random_blackout_before_number = random.randint(0, 15)
        random_blackout_before = (random_blackout_before_number > 3)

        delay = 0.1

        # Calculate delay - More segments = less delay
        for ignored_delay_loop in range(0, random_segment_count):
            delay -= 0.007

        for ignored_count_loop in range(0, 50):
            display_segments(strip, get_segments(random_segment_count, random_segment_order), delay,
                             blackout_before=random_blackout_before,
                             random_colour_allow_black=(random_blackout_before == True))
