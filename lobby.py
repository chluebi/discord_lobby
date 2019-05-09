
import discord
import util


# This class is meant for typical teamgames and 1v1s
#
#
#

class Teamlobby():

    # Example:
    # game = TeamLobby(channel)

    def __init__(self, channel):

        self.channel = channel
        self.teams = {}       # we save the players in a dictionary to group them by teams

    def add_team(self, name):

        self.teams[name] = {}
        self.teams[name]['id'] = len(self.teams.iteritems()) + 1  # compensate to the thing added

    def get_team(self, name):
        found_team = None
        for team, content in self.teams.items():
            if team == name:
                found_team =
                break

    def join(self, teamid):
        pass
