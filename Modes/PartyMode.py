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

from Effects.Party import *
from Modes.Util.ModeUtil import *

instance = None
effects = [SingleRainbowCycleStrobeEffect, SingleRGBCycleStrobeEffect, MultipleRainbowCycleStrobeEffect,
           SingleRandomColourEffect, SingleRandomColourStrobeEffect, SingleRandomColourMultiStrobeEffect,
           SingleRandomColourSlowMultiStrobeEffect, SingleRandomColourSlowStrobeEffect,
           DualAlternatingPixelRandomEffect, DualAlternatingPixelRandomStrobeEffect,
           DualSplitRandomEffect, DualSplitRandomStrobeEffect,
           DualSplitSynchronizedRandomEffect, DualSplitSynchronizedRandomStrobeEffect,
           TriSplitRandomEffect, TriSplitRandomStrobeEffect,
           TriSplitSynchronizedRandomEffect, TriSplitSynchronizedRandomStrobeEffect,
           FourSplitRandomEffect, FourSplitRandomStrobeEffect,
           FourSplitSynchronizedRandomEffect, FourSplitSynchronizedRandomStrobeEffect,
           DualSplitMovingRandomEffect,
           TenSplitMiddleToEndRandomColourEffect, TenSplitMiddleToEndRandomColourStrobeEffect,
           TenSplitEndToMiddleRandomColourEffect, TenSplitEndToMiddleRandomColourStrobeEffect,
           TenSplitMiddleToEndRandomLoopColourEffect, TenSplitMiddleToEndRandomLoopColourStrobeEffect,
           TenSplitEndToMiddleRandomLoopColourEffect, TenSplitEndToMiddleRandomLoopColourStrobeEffect,
           TenSplitStartToEndRandomLoopColourEffect, TenSplitStartToEndRandomColourEffect,
           SingleRandomColourFastFadeOutEffect, SingleRandomColourFastFadeInEffect]


def set_instance(PiLED):
    global instance
    instance = PiLED


def run():
    global instance
    global effects

    while True:
        run_random_mode(effects, instance)
