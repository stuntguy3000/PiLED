'''

https://github.com/Erlendeikeland/csgo-gsi-python

MIT License

Copyright (c) 2019 Erlend

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from operator import attrgetter
from threading import Thread

from Lib.CSGO.CSGOGamestate import GameStateClass
from Lib.CSGO.CSGOPayloadParser import PayloadParserClass
from Lib.CSGO.CSGOEventProcessor import EventProcessorClass


class GSIServer(HTTPServer):
    # stuntguy3000 - Add event handler callback function
    def __init__(self, server_address, auth_token, instance):
        super(GSIServer, self).__init__(server_address, RequestHandler)

        self.auth_token = auth_token
        self.gamestate = GameStateClass()
        self.parser = PayloadParserClass()
        self.events = EventProcessorClass(instance)

        self.instance = instance

    def start_server(self):
        try:
            thread = Thread(target=self.serve_forever)
            thread.start()
            # stuntguy3000 - Added prefix
            print("[CSGOGSIServer] Server started.")
        except:
            # stuntguy3000 - Added prefix to error message and program halt
            print("[CSGOGSIServer] Could not start server.")
            exit(1)

    def get_info(self, target, *argv):
        try:
            # stuntguy3000 - Syntax errors are being thrown... replacing string format
            if len(argv) == 0:
                state = attrgetter("{}".format(self.gamestate))
            elif len(argv) == 1:
                state = attrgetter("{}.{}".format(self.gamestate, argv[0]))
            elif len(argv) == 2:
                state = attrgetter("{}.{}".format(self.gamestate, argv[1]))
            else:
                # stuntguy3000 - Added prefix to error message
                print("[CSGOGSIServer] Too many arguments.")
                return False
            if "object" in str(state):
                return vars(state)
            else:
                return state
        except Exception as E:
            print(E)
            return False


class RequestHandler(BaseHTTPRequestHandler):
    current_effect_thread = None

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode("utf-8")

        payload = json.loads(body)

        if not self.authenticate_payload(payload):
            # stuntguy3000 - Added prefix to error message
            print("[CSGOGSIServer] auth_token does not match.")
            return False
        else:
            self.server.running = True

        self.server.parser.parse_payload(payload, self.server.gamestate)
        self.server.events.process_gamestate(self.server.gamestate)

    def authenticate_payload(self, payload):
        if "auth" in payload and "token" in payload["auth"]:
            return payload["auth"]["token"] == self.server.auth_token
        else:
            return False

