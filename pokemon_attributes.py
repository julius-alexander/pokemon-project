# attributes will have the form:
# pokemon_name = 'name', ID, moves, types, base_stats, exp, ivs, evs, nature, ability

from random import randint
from math import floor
import mysql.connector

# Enter appropriate information below
myPokeStatsDB = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

myCursor = myPokeStatsDB.cursor()


Natures = {
    0: 'Hardy',
    1: 'Lonely',
    2: 'Brave',
    3: 'Adamant',
    4: 'Naughty',
    5: 'Bold',
    6: 'Docile',
    7: 'Relaxed',
    8: 'Impish',
    9: 'Lax',
    10: 'Timid',
    11: 'Hasty',
    12: 'Serious',
    13: 'Jolly',
    14: 'Naive',
    15: 'Modest',
    16: 'Mild',
    17: 'Quiet',
    18: 'Bashful',
    19: 'Rash',
    20: 'Calm',
    21: 'Gentle',
    22: 'Sassy',
    23: 'Careful',
    24: 'Quirky'

}


class Moves:
    def __init__(self, name):
        self.name = name
        self.type = 0
        self.category = 0
        self.power = 0
        self.accuracy = 0
        self.power_points = 0
        self.effect = 0

    def set_pp(self):
        pass


# res will be a list in the following format:
# [id, name, type1, type2, total, hp, atk, def, spatk, spdef, speed, generation, legendary]
class PokeMon:

    def __init__(self, res):
        self.ivs =        [randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31)]
        self.id =         res[0]
        self.base_stats = [res[5], res[6], res[7], res[8], res[9], res[10]]
        self.evs =        [0, 0, 0, 0, 0, 0]
        self.nature =     randint(0, 24)
        self.level =      100
        self.moves =      [0, 0, 0, 0]
        self.name =       res[1]

        # Below are the main series' formulas for calculating the 6 major stats at each level
        self.hp =              (floor(0.01 * (2 * self.base_stats[0] + self.ivs[0]) * self.level) + self.level + 10)
        self.attack =          (floor(0.01 * (2 * self.base_stats[1] + self.ivs[1]) * self.level) + 5)
        self.defense =         (floor(0.01 * (2 * self.base_stats[2] + self.ivs[2]) * self.level) + 5)
        self.special_attack =  (floor(0.01 * (2 * self.base_stats[3] + self.ivs[3]) * self.level) + 5)
        self.special_defense = (floor(0.01 * (2 * self.base_stats[4] + self.ivs[4]) * self.level) + 5)
        self.speed =           (floor(0.01 * (2 * self.base_stats[5] + self.ivs[5]) * self.level) + 5)

        self.set_nature_stats()

    def set_stats(self, evs):
        self.hp =              (floor(0.01 * (2 * self.base_stats[0] + self.ivs[0] + floor(0.25 * evs[0])) * self.level) + self.level + 10)
        self.attack =          (floor(0.01 * (2 * self.base_stats[1] + self.ivs[1] + floor(0.25 * evs[1])) * self.level) + 5)
        self.defense =         (floor(0.01 * (2 * self.base_stats[2] + self.ivs[2] + floor(0.25 * evs[2])) * self.level) + 5)
        self.special_attack =  (floor(0.01 * (2 * self.base_stats[3] + self.ivs[3] + floor(0.25 * evs[3])) * self.level) + 5)
        self.special_defense = (floor(0.01 * (2 * self.base_stats[4] + self.ivs[4] + floor(0.25 * evs[4])) * self.level) + 5)
        self.speed =           (floor(0.01 * (2 * self.base_stats[5] + self.ivs[5] + floor(0.25 * evs[5])) * self.level) + 5)

    def set_nature_stats(self):
        # Lonely, Brave, Adamant, Naughty: 1-4, respectively
        if self.nature in [1, 2, 3, 4]:
            self.attack = floor(self.attack * 1.1)

            if self.nature == 1:
                self.defense = floor(self.defense * 0.9)
            elif self.nature == 2:
                self.speed = floor(self.speed * 0.9)
            elif self.nature == 3:
                self.special_attack = floor(self.special_attack * 0.9)
            elif self.nature == 4:
                self.special_defense = floor(self.special_defense * 0.9)

        # Bold, Relaxed, Impish, Lax: 5, 7, 8, 9, respectively
        elif self.nature in [5, 7, 8, 9]:
            self.defense = floor(self.defense * 1.1)

            if self.nature == 5:
                self.attack = floor(self.attack * 0.9)
            elif self.nature == 7:
                self.speed = floor(self.speed * 0.9)
            elif self.nature == 8:
                self.special_attack = floor(self.special_attack * 0.9)
            elif self.nature == 9:
                self.special_defense = floor(self.special_defense * 0.9)

        # Timid, Hasty, Jolly, Naive: 10, 11, 13, 14, respectively
        elif self.nature in [10, 11, 13, 14]:
            self.speed = floor(self.speed * 1.1)

            if self.nature == 10:
                self.attack = floor(self.attack * 0.9)
            elif self.nature == 11:
                self.defense = floor(self.defense * 0.9)
            elif self.nature == 13:
                self.special_attack = floor(self.special_attack * 0.9)
            elif self.nature == 14:
                self.special_defense = floor(self.special_defense * 0.9)

        # Modest, Mild, Quiet, Rash: 15, 16, 17, 19, respectively
        elif self.nature in [15, 16, 17, 19]:
            self.special_attack = floor(self.special_attack * 1.1)

            if self.nature == 15:
                self.attack = floor(self.attack * 0.9)
            elif self.nature == 16:
                self.defense = floor(self.defense * 0.9)
            elif self.nature == 17:
                self.speed = floor(self.speed * 0.9)
            elif self.nature == 19:
                self.special_defense = floor(self.special_defense * 0.9)

        # Calm, Gentle, Sassy, Careful: 20, 21, 22, 23, respectively
        elif self.nature in [20, 21, 22, 23]:
            self.special_defense = floor(self.special_defense * 1.1)

            if self.nature == 20:
                self.attack = floor(self.attack * 0.9)
            elif self.nature == 21:
                self.defense = floor(self.defense * 0.9)
            elif self.nature == 22:
                self.speed = floor(self.speed * 0.9)
            elif self.nature == 23:
                self.special_attack = floor(self.special_attack * 0.9)

    def set_ivs(self, x):
        self.ivs = x

    def __str__(self):
        return f'\nPokeMon Name:  {self.name}\n' \
               f'PokeDex Entry: {self.id:0>3}\n' \
               f'LVL.    {self.level}\n' \
               f'Nature: {Natures[self.nature]}\n\n' \
               f'Stats:\n' \
               f'HP:     {self.hp:0>3}  '\
               f'SPD:    {self.speed:0>3}\n'\
               f'ATK:    {self.attack:0>3}  '\
               f'DEF:    {self.defense:0>3}\n' \
               f'SP.ATK: {self.special_attack:0>3}  ' \
               f'SP.DEF: {self.special_defense:0>3}\n'


def update_poke_stats():
    pass  # needs to have capabilities adjusting EVs and IVs -- maybe Natures too
