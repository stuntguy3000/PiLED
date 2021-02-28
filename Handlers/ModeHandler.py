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

# import traceback
import multiprocessing

from Modes import BlackoutMode
from Modes import OffMode
from Modes import NormalMode
from Modes import PartyMode
from Modes import PoliceMode
from Modes import SingleColourMode
from Modes import SingleFlashMode
from Modes import SlowFadeInMode
from Modes import SlowFadeOutMode
from Modes import FireMode

instance = None
current_mode_thread = None


class ModeHandlerClass:
    MODE_MAP = {
        'NORMAL': NormalMode,
        'PARTY': PartyMode,
        'SINGLE_COLOUR': SingleColourMode,
        'SINGLE_FLASH': SingleFlashMode,
        'POLICE': PoliceMode,
        'BLACKOUT': BlackoutMode,
        'OFF': OffMode,
        'SLOWFADEOUT': SlowFadeOutMode,
        'SLOWFADEIN': SlowFadeInMode,
        'FIRE': FireMode,
    }

    def init(self, PiLED):
        # Whatever initialising means...
        print("[ModeHandler] Mode handler initialising.")

        global instance
        instance = PiLED

        self.run_mode("OFF")

    def run_mode(self, mode_name):
        mode_name = str.upper(mode_name)

        try:
            # Setup mode to be run
            function_class = self.MODE_MAP[mode_name]
            function_class.set_instance(instance)
            run_mode_function = getattr(function_class, "run")

            # Run new mode in it's own thread
            print("[ModeHandler] Running mode \"" + mode_name + "\"")
            self.stop_current_mode()

            global current_mode_thread
            current_mode_thread = multiprocessing.Process(target=run_mode_function)
            current_mode_thread.start()

            # We're done here.
            return True
        except KeyError:
            print("[ModeHandler] Unable to run mode \"" + mode_name + "\". Does it exist?")
            # traceback.print_exc()

        return False

    def stop_current_mode(self):
        global current_mode_thread
        if current_mode_thread is not None:
            current_mode_thread.terminate()
