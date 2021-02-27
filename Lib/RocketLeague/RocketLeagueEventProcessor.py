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

import multiprocessing

from Effects.RocketLeague import *
from Lib.RocketLeague.RocketLeagueGamestate import GameStateClass
from Modes.Util.ModeUtil import *


class EventProcessorClass:
    instance = None
    current_effect_thread = None

    last_gamestate_status = 0
    reset_background = 1

    goals_teamblue = 0
    goals_teamorange = 0

    def __init__(self, instance):
        self.instance = instance

    def event_menu(self):
        print("event_menu")
        self.run_mode_on_thread(RocketLeagueMenuEffect)

    def event_ingame_teamblue(self):
        print("event_ingame_teamblue")
        self.run_mode_on_thread(RocketLeagueBlueTeamEffect)

    def event_ingame_teamorange(self):
        print("event_ingame_teamorange")
        self.run_mode_on_thread(RocketLeagueOrangeTeamEffect)

    def event_ingame_teamblue_goal(self):
        print("event_ingame_teamblue_goal")
        self.run_mode_on_thread(RocketLeagueBlueTeamGoalEffect)

    def event_ingame_teamorange_goal(self):
        print("event_ingame_teamorange_goal")
        self.run_mode_on_thread(RocketLeagueOrangeTeamGoalEffect)

    def process_gamestate(self, gamestate: GameStateClass):
        # Process menu state
        print("Processing effect...")

        if gamestate is not None:
            if gamestate.game.status == -1 and self.last_gamestate_status is not -1:
                self.last_gamestate_status = -1
                self.reset_background = 1

                self.goals_teamblue = 0
                self.goals_teamorange = 0

                self.event_menu()
            elif gamestate.game.status == 1:
                self.last_gamestate_status = 1

                # Reset the background if required
                if self.reset_background == 1:
                    self.reset_background = 0

                    if gamestate.player.team == 0:
                        self.event_ingame_teamblue()
                    else:
                        self.event_ingame_teamorange()

                # Test if a goal has been scored
                print("Goals: " + str(gamestate.match.team_0["goals"]) +
                      " (" + str(self.goals_teamblue) + ") "
                      + str(gamestate.match.team_1["goals"])
                      + " (" + str(self.goals_teamorange) + ") ")

                if gamestate.match.team_0["goals"] > self.goals_teamblue:
                    self.goals_teamblue = gamestate.match.team_0["goals"]
                    self.event_ingame_teamblue_goal()
                    self.reset_background = 1
                elif gamestate.match.team_1["goals"] > self.goals_teamorange:
                    self.goals_teamorange = gamestate.match.team_1["goals"]
                    self.event_ingame_teamorange_goal()
                    self.reset_background = 1

    def run_mode_on_thread(self, effect_class):
        # Stop current effect thread
        if self.current_effect_thread is not None:
            print("Terminating current thread...")
            self.current_effect_thread.terminate()
        else:
            print("No thread to terminate...")

        # Process the RocketLeague Gamestate
        self.current_effect_thread = multiprocessing.Process(target=run_mode, args=[effect_class, self.instance])
        self.current_effect_thread.start()
