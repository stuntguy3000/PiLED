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

import http.server
import re
import socketserver

instance = None

class WebserverHandlerClass():
    WEBSERVER_HOST = "LukePi"
    WEBSERVER_PORT = 1337

    def init(self, PiLED):
        print("[WebserverHandler] Starting web server at address http://" + self.WEBSERVER_HOST + ":" + str(
            self.WEBSERVER_PORT) + "/")
        socketserver.TCPServer.allow_reuse_address = True

        # Set Instance
        global instance
        instance = PiLED

        server = socketserver.ThreadingTCPServer(('', self.WEBSERVER_PORT), WebserverResponseHandlerClass)
        server.serve_forever()
        print("[WebserverHandler] Web server running.")


class WebserverResponseHandlerClass(http.server.SimpleHTTPRequestHandler):
    REGEX_MODE = "/mode/([A-z]+)"
    REGEX_MODELIST = "/modelist"

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        print("[WebserverHandler] Incoming Request: " + self.path)

        mode_request_regex = re.match(self.REGEX_MODE, self.path)
        # Is it a mode change request?
        if mode_request_regex is not None:
            # Process mode change request
            global instance
            result = instance.ModeHandlerInstance.run_mode(mode_request_regex.group(1))

            # Process Return
            if result:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                self.wfile.write(("Changing into mode " + str(mode_request_regex.group(1)) + ".").encode("utf-8"))
            else:
                self.send_error(404, "Mode not found.")

            return

        mode_list_request_regex = re.match(self.REGEX_MODELIST, self.path)
        # Is it a mode list request?
        if mode_list_request_regex is not None:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # todo
            # make work
