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

instance = None

server = None
SERVER_IP = "127.0.0.1"
SERVER_PORT = 3000
GSI_KEY = "PiLED"

def run(PiLED):
    global instance
    instance = PiLED

    # Start GSI Server
    print("[CSGOGSIHandler] Starting GSI Server on " + SERVER_IP + ":" + GSI_KEY)
    global server
    server = GSIServer((SERVER_IP, SERVER_PORT), SERVER_KEY)
    server.start_server()

    # Would be nice to do event based programming, and it's probably possible, but oh well......................maybe
    # Instead, we will need to check the gamestate constantly
    #
    # unless i modify the bloody API
    #
    # maybe
    # #effort
