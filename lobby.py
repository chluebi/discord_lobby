
import discord
import util


# This class is meant for typical teamgames and 1v1s
#
#
#

class Teamlobby():

    # Example:
    # game = TeamLobby(channel)

    def __init__(self, channel, creator=None, prefix='!'):

        self.channel = channel
        self.teams = []  # we save the players in a dictionary to group them by teams
        if creator is not None:
            self.admins = [Player(creator)]  # we need someone to control the game
        else:
            self.admins = []
        self.prefix = prefix
        self.stage = 'prejoin'

    # ADMIN STUFF
    def add_admin(self, player):
        self.admins.append(Player(player))

    def remove_admin(self, id):
        for player in self.admins:
            if player.user.id == id:
                self.admins.remove(player)

    def get_admin(self, playername):
        found_admin = None
        for player in self.admins:
            if player == playername:
                found_admin = player

        if found_admin is None:
            raise util.Team.PlayerNotFound('Player {} not found in {}'.format(playername, self))

        return found_admin

    def add_team(self, name=None):
        if name is None:
            name = 'Team ' + len(self.teams)

        new_team = util.Team(name)
        new_team.id = len(self.teams)
        self.teams.append(new_team)

    def get_team(self, name):
        found_team = None
        for team in self.teams:
            if team == name:
                found_team = team
                break

        return found_team

    def join(self, teamid):
        pass
