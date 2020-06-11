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

from Lib.CSGO.CSGOGamestate import GameStateClass

from Effects.CSGO import *
from Modes.Util.ModeUtil import *

import multiprocessing

class EventProcessorClass:
    state_player_in_menu = False
    state_round_winteam = False
    state_round_bomb_planted = False
    state_player_dead = False
    state_player_team = None
    team_background_update_required = True

    instance = None
    current_effect_thread = None

    def __init__(self, instance):
        self.instance = instance

    def process_gamestate(self, gamestate: GameStateClass):
        # Process menu state
        print("Processing effect...")

        if gamestate.player.activity == "menu":
            if self.state_player_in_menu:
                return

            self.state_player_in_menu = True
            self.team_background_update_required = True
            self.state_player_team = None
            self.event_inmenu()
            return
        else:
            # Reset states
            self.state_player_in_menu = False

            # Process round state
            if gamestate.round.phase == "over":
                if self.state_round_winteam:
                    return

                if gamestate.round.win_team == "T":
                    self.event_ingame_round_win_t()
                elif gamestate.round.win_team == "CT":
                    self.event_ingame_round_win_ct()

                self.state_round_winteam = True
                self.team_background_update_required = True
                self.state_player_team = None
            else:
                # Reset states
                self.state_round_winteam = False

                # Process if the bomb is planted
                if gamestate.round.bomb is not None and gamestate.round.bomb == "planted":
                    if not self.state_round_bomb_planted:
                        self.event_ingame_bomb_planted()

                        self.state_round_bomb_planted = True
                        self.team_background_update_required = True
                else:
                    # Reset states
                    self.state_round_bomb_planted = False

                    # Determine if player has died
                    if self.state_player_team is not None and gamestate.player.state['health'] == 0:
                        if self.state_player_dead:
                            return

                        self.state_player_dead = True
                        self.event_ingame_player_dead()
                        return

                    # If they've hit this point, they ain't dead! Force an update
                    if self.state_player_dead:
                        self.team_background_update_required = True
                        self.state_player_dead = False

                    # If they've changed teams (either by speccing another player or actually changing teams),
                    # Force an update
                    current_team = gamestate.player.team

                    if current_team != self.state_player_team:
                        self.team_background_update_required = True

                    # Display team colour only when needed
                    if self.team_background_update_required:
                        if gamestate.player.team == "T":
                            self.event_ingame_playing_team_t()
                        elif gamestate.player.team == "CT":
                            self.event_ingame_playing_team_ct()

                        self.state_player_team = gamestate.player.team
                        self.team_background_update_required = False

    def event_inmenu(self):
        print("event_inmenu")
        self.run_mode_on_thread(CSGOMenuEffect)

    def event_ingame_round_win_t(self):
        print("event_ingame_round_win_t")
        self.run_mode_on_thread(CSGOTeamTWinEffect)

    def event_ingame_round_win_ct(self):
        print("event_ingame_round_win_ct")
        self.run_mode_on_thread(CSGOTeamCTWinEffect)

    def event_ingame_playing_team_t(self):
        print("event_ingame_playing_team_t")
        self.run_mode_on_thread(CSGOTeamTEffect)

    def event_ingame_playing_team_ct(self):
        print("event_ingame_playing_team_ct")
        self.run_mode_on_thread(CSGOTeamCTEffect)

    def event_ingame_player_dead(self):
        print("event_ingame_player_dead")
        self.run_mode_on_thread(CSGODeathEffect)

    def event_ingame_bomb_planted(self):
        print("event_ingame_bomb_planted")

    def run_mode_on_thread(self, effect_class):
        # Stop current effect thread
        if self.current_effect_thread is not None:
            print("Terminating current thread...")
            self.current_effect_thread.terminate()
        else:
            print("No thread to terminate...")

        # Process the CSGO Gamestate
        self.current_effect_thread = multiprocessing.Process(target=run_mode, args=[effect_class, self.instance])
        self.current_effect_thread.start()