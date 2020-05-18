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

from Lib.CSGO.CSGOServer import GSIServer

instance = None
server = None

SERVER_IP = ""
SERVER_PORT = 3000
GSI_KEY = "PiLED"


def event_handler():
    global instance
    global server
    print("CS:GO Event Received!")


class CSGOGSIHandlerClass:
    def run(self, PiLED):
        global instance
        global server
        global SERVER_IP
        global SERVER_PORT
        global GSI_KEY

        instance = PiLED

        # Start GSI Server
        print("[CSGOGSIHandler] Starting GSI Server on \"" + SERVER_IP + ":" + str(SERVER_PORT) + "\"")

        server = GSIServer((SERVER_IP, SERVER_PORT), GSI_KEY, event_handler)
        server.start_server()
