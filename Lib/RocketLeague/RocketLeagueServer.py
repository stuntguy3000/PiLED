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

import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from operator import attrgetter
from threading import Thread

from Lib.RocketLeague.RocketLeagueGamestate import GameStateClass
from Lib.RocketLeague.RocketLeaguePayloadParser import PayloadParserClass
from Lib.RocketLeague.RocketLeagueEventProcessor import EventProcessorClass

class GSIServer(HTTPServer):
    def __init__(self, server_address, instance):
        super(GSIServer, self).__init__(server_address, RequestHandler)

        self.gamestate = GameStateClass()
        self.parser = PayloadParserClass()
        self.events = EventProcessorClass(instance)

        self.instance = instance

    def start_server(self):
        try:
            thread = Thread(target=self.serve_forever)
            thread.start()
            print("[RocketLeagueGSIServer] Server started.")
        except:
            print("[RocketLeagueGSIServer] Could not start server.")
            exit(1)


class RequestHandler(BaseHTTPRequestHandler):
    current_effect_thread = None

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode("utf-8")

        payload = json.loads(body)

        self.server.running = True
        self.server.parser.parse_payload(payload, self.server.gamestate)
        self.server.events.process_gamestate(self.server.gamestate)
