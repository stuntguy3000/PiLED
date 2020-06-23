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

from typing import List
import json


class Game:
    def __init__(self):
        self.status = -1


class Match:
    def __init__(self):
        self.playlist = -1
        self.time = -1
        self.team_0 = None
        self.team_1 = None

"""
class MatchTeam:
    def __init__(self):
        self.blue = 0
        self.red = 0
        self.green = 0
        self.goals = 0
        self.name = ""
"""

class Player:
    def __init__(self):
        self.assists = -1
        self.boost = -1.0
        self.goals = -1
        self.saves = -1
        self.score = -1
        self.shots = -1
        self.team = -1


class Provider:
    def __init__(self):
        self.appid = None
        self.name = None
