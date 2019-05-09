from discord import User, Member
import discord.utils


# This file has the base classes


class Player():

    class NoDiscordUserPassed(Exception):
        ''' Raised when the user passed into the constructor isn\'t from discord '''
        pass

    def __init__(self, discorduser):
        print(type(discorduser))
        if type(discorduser) not in [User, Member]:
            raise Player.NoDiscordUserPassed()

        self.user = discorduser


class Team():

    class PlayerNotFound(Exception):
        ''' Raised when a player is not found by for example get_player()'''
        pass

    def __init__(self, name, creator):
        self.name = name
        self.players = []
        self.admins = [Player(creator)]  # We need someone to be able to control the game

    # PLAYER STUFF
    def add_player(self, player):
        self.players.append(Player(player))

    def remove_player(self, id):
        for player in self.players:
            if player.user.id == id:
                self.players.remove(player)

    def get_player(self, playername):
        found_player = None
        for player in self.players:
            if player == playername:
                found_player = player

        if found_player is None:
            raise Team.PlayerNotFound('Player {} not found in {}'.format(playername, self))

        return found_player

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
            raise Team.PlayerNotFound('Player {} not found in {}'.format(playername, self))

        return found_admin

    # METRICS
    # Basically they are attributes of all players in that team

    def add_metric(self, metricname, value=None):
        for player in self.players:
            setattr(player, metricname, value)

    def metriclist(self, metricname):
        endlist = []
        for player in self.players:
            endlist.append((player, getattr(player, metricname)))

        return endlist

    def metricsum(self, metricname):
        endsum = 0
        for player in self.players:
            endsum += getattr(player, metricname)

        return endsum
