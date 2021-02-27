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

# -------------------------------------------------------------------------------------------
#  ____  _ _     _____ ____
# |  _ \(_) |   | ____|  _ \
# | |_) | | |   |  _| | | | |
# |  __/| | |___| |___| |_| |
# |_|   |_|_____|_____|____/
#
# PiLED by stuntguy3000
#
# A very basic set of Python scripts to power and control WS2812B LEDs using a Raspberry Pi.
# -------------------------------------------------------------------------------------------

class PiLEDClass:
    def __init__(self):
        # Import Classes
        from Handlers import LEDHandler
        from Handlers import ModeHandler
        from Handlers import WebserverHandler

        self.LEDHandlerInstance = LEDHandler.LEDHandlerClass()
        self.ModeHandlerInstance = ModeHandler.ModeHandlerClass()
        self.WebserverHandlerInstance = WebserverHandler.WebserverHandlerClass()

    def setup_handlers(self):
        # Start LEDs
        self.LEDHandlerInstance.init(instance)

        # Start Mode Handler
        self.ModeHandlerInstance.init(instance)

        # Start Webserver
        self.WebserverHandlerInstance.init(instance)

    def load(self):
        # Begin Execution
        print("")
        print("  ____  _ _     _____ ____")
        print(" |  _ \(_) |   | ____|  _ \\")
        print(" | |_) | | |   |  _| | | | |")
        print(" |  __/| | |___| |___| |_| |")
        print(" |_|   |_|_____|_____|____/")
        print("")
        print("PiLED by stuntguy3000.")
        print("")
        print("")

        print("[PiLED] Starting handlers...")
        self.setup_handlers()


if __name__ == "__main__":
    # Run it
    # https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it
    instance = PiLEDClass()
    instance.load()
