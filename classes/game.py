import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FATL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




class Person:
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_heal(self, dmg):
        self.hp += dmg
        return  self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost


    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("      " + str(i) + ":" , item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("      " + str(i) + ":", spell.name, "(cost:" , str(spell.cost) , ")")
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "ITEM:" + bcolors.ENDC)
        for item in self.items:
            print("      " + str(i) + " :", item["item"].name, ";", item["item"].description, ",",
                  bcolors.OKBLUE + bcolors.BOLD, str(item["quantity"]) + "x", bcolors.ENDC )
            i += 1


    def get_stats(self):

        hp_bar = int( self.hp / self.maxhp * 100 / 4)
        hp_fill = ""

        while hp_bar > 0:
            hp_fill += "|"
            hp_bar -= 1

        while len(hp_fill) < 25:
            hp_fill += " "

        mp_bar = int( self.mp / self.maxmp * 100 / 10)
        mp_fill = ""

        while mp_bar > 0:
            mp_fill += "|"
            mp_bar -= 1

        while len(mp_fill) < 10:
            mp_fill += " "

        character_name = self.name + ":"
        player_white_space = ""

        while len(character_name) < 15:
            player_white_space += " "
            character_name = self.name + ":" + player_white_space

        hp_fraction = str(self.hp) + "/" + str(self.maxhp)
        mp_fraction = str(self.mp) + "/" + str(self.maxmp)

        while len(hp_fraction) < 12:
            hp_fraction_space = " "
            hp_fraction += hp_fraction_space

        while len(mp_fraction) < 6:
            mp_fraction_space = " "
            mp_fraction += mp_fraction_space

        print("   "+ character_name + hp_fraction + "[" + bcolors.FATL +
              bcolors.BOLD + hp_fill + bcolors.ENDC + "]" + "" + "" + " ,     " + mp_fraction +
              "" + "[" + bcolors.FATL + bcolors.BOLD + mp_fill + bcolors.ENDC + "]", "\n")



    def get_enemy_stats(self):

        hp_bar = int(self.hp / self.maxhp * 100 / 2)
        hp_fill = ""

        while hp_bar > 0:
            hp_fill += "|"
            hp_bar -= 1

        while len(hp_fill) < 50:
            hp_fill += " "

        character_name = self.name + ":"
        enemy_white_space = ""

        while len(character_name) < 15:
            enemy_white_space += " "
            character_name = self.name + ":" + enemy_white_space

        hp_fraction = str(self.hp) + "/" + str(self.maxhp)
        hp_fraction_space = ""

        while len(hp_fraction) < 12:
            hp_fraction_space = " "
            hp_fraction += hp_fraction_space

        print("   "+ character_name + hp_fraction + "[" + bcolors.FATL +
              bcolors.BOLD + hp_fill + bcolors.ENDC + "]" + "\n")


    def enemy_choose_spell(self):
        magic_choice = random.randrange(0,len(self.magic))
        spell_choice = self.magic[magic_choice]
        return spell_choice


