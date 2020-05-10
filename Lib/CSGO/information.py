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


"""
Classes to represent Player information
"""
class Player:
    """Class to store player information"""
    def __init__(self):
        self.name = None
        self.activity = None
        self.forward = None
        self.position = None
        self.observer_slot = None
        self.team = None
        self.clan = None
        self.steamid = None
        self.spectarget = None
        self.state = State()
        self.match_stats = MatchStats()
        self.weapons = {}

class State:
    """Class to store player state information"""
    def __init__(self):
        self.armor = None
        self.burning = None
        self.equip_value = None
        self.flashed = None
        self.health = None
        self.helmet = None
        self.money = None
        self.round_killhs = None
        self.round_kills = None
        self.round_totaldmg = None
        self.smoked = None

class MatchStats:
    """Class to store player match stats information"""
    def __init__(self):
        self.assists = None
        self.deaths = None
        self.kills = None
        self.mvps = None
        self.score = None


"""
Classes to represent Map information
"""
class Map:
    """Class to store map information"""
    def __init__(self):
        self.round_wins = None
        self.current_spectators = None
        self.mode = None
        self.name = None
        self.num_matches_to_win_series = None
        self.phase = None
        self.round = None
        self.souvenirs_total = None
        self.team_ct = Team()
        self.team_t = Team()

class Team:
    """Class to store map teams information"""
    def __init__(self):
        self.consecutive_round_losses = None
        self.matches_won_this_series = None
        self.score = None
        self.name = None
        self.timeouts_remaining = None


"""
Class to represent Provider information
"""
class Provider:
    """Class to store provider information"""
    def __init__(self):
        self.appid = None
        self.name = None
        self.steamid = None
        self.timestamp = None
        self.version = None
        self.update_info = None


"""
Class to represent Phase Countdowns information
"""
class PhaseCountdowns:
    """Class to store phase countdowns information"""
    def __init__(self):
        self.phase = None
        self.phase_ends_in = None


"""
Class to represent Bomb information
"""
class Bomb:
    """Class to store bomb information"""
    def __init__(self):
        self.player = None
        self.position = None
        self.state = None
        self.countdown = None


"""
Class to represent Round information
"""
class Round:
    """Class to store round information"""
    def __init__(self):
        self.phase = None
        self.win_team = None
        self.bomb = None
