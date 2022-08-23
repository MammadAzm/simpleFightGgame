
import  random

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


#create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi_Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 99999)
hielixer = Item("MegaElixer", "elixer", "Fully restores the party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 points of damage", 500)

player_magic =  [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, cure]

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 10}, {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 2}]

#Instantiate People
player1 = Person("Alpha", 460, 65, 60, 34, player_magic , player_items)
player2 = Person("Beta", 460, 65, 60, 34, player_magic , player_items)

enemy1 = Person("Gama", 1200, 65, 45, 25, enemy_magic, [])
enemy2 = Person("Lynda", 1200, 65, 45, 25, enemy_magic, [])
Players = [player1, player2]
Enemies = [enemy1, enemy2]

Players_number = 0
Enemies_number = 0
for player in Players:
    Players_number += 1
for enemy in Enemies:
    Enemies_number += 1

running = True
i = 0

print(bcolors.FATL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===========================")
    print(bcolors.OKBLUE + "    NAME                              HP                               MP" + "\n" + bcolors.ENDC)

    for player in Players:
        player.get_stats()

    for enemy in Enemies:
        enemy.get_enemy_stats()



    for player in Players:
        if Players_number == 0:
            pass
        elif Enemies_number == 0:
            pass
        player.choose_action()
        choice = input("\n"+ player.name + ", " + "Choose Action:")
        index = int(choice) - 1

        player_target = random.randrange(0 , Enemies_number)


        if index == 0:
            dmg = player.generate_damage()
            Enemies[player_target].take_damage(dmg)
            print("You attacked for ", dmg, "points of damage.")
            if Enemies[player_target].hp <= 0:
                print(bcolors.FATL, Enemies[player_target].name , "has died." + bcolors.ENDC)
                del Enemies[player_target]
                Enemies_number -= 1
                if Enemies_number == 0:
                    print("\n\n")
                    print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                    print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                    print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
                    print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                    print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                    running = False
                elif Players_number == 0:
                    print("\n\n")
                    print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                    print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                    print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
                    print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                    print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                    running = False




        elif index == 1:
            print("You chose magic, please select the spell you wanna buy:")
            player.choose_magic()
            magic_choice = int(input("\nchoose magic.")) - 1

            if magic_choice == -1:
                i = 0
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            spell_cost = spell.cost
            current_mp = player.get_mp()

            if current_mp < spell_cost:
                print(bcolors.FATL + "\nYou have not enough mp to purchase this spell.\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell_cost)

            if spell.type == "black":
                Enemies[player_target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name, " deals", str(magic_dmg), "points of damage out of your enemy." + bcolors.ENDC)
                if Enemies[player_target].hp <= 0:
                    print(bcolors.FATL, Enemies[player_target].name, "has died." + bcolors.ENDC)
                    del Enemies[player_target]
                    Enemies_number -= 1
                    if Enemies_number == 0:
                        print("\n\n")
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        running = False
                    elif Players_number == 0:
                        print("\n\n")
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        running = False



            elif spell.type == "white":
                player.take_heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name, " healed your HP for " , str(magic_dmg), " points." + bcolors.ENDC)
                if player.hp > player.maxhp:
                    player.hp = player.maxhp
                    print("Your HP is now full.")



        elif index == 2:
            print("------------------------------------")
            print("You chose Items, please select the item you wanna take:")
            print("------------------------------------")

            player.choose_item()

            print("------------------------------------")
            item_choice = int(input("Choose item: ")) - 1
            print("------------------------------------")

            if item_choice == -1:
                i = 0
                continue

            item = player.items[item_choice]["item"]


            if item.type == "potion":
                if player.items[item_choice]["quantity"] > 0:
                    player.take_heal(item.prop)
                    print(bcolors.OKBLUE, item.name, "healed your HP for", item.prop, "points.", bcolors.ENDC)
                    if player.hp > player.maxhp:
                        player.hp = player.maxhp
                        print(bcolors.OKGREEN + bcolors.BOLD, "Your HP is now full.", bcolors.ENDC)
                    potion_quantity = player.items[item_choice]["quantity"]
                    print(bcolors.OKBLUE + bcolors.BOLD,"Left ", item.name, ":" , str(int(potion_quantity) -1)+ "x", bcolors.ENDC)
                else:
                    print(bcolors.FATL + bcolors.BOLD, "You have no", item.name, ".", bcolors.ENDC)
                    continue

            elif item.type == "elixer":
                if item.name == "Elixer":
                    if player.items[item_choice]["quantity"] > 0:
                        player.mp = player.maxmp
                        player.hp = player.maxhp
                        elixer_quantity = player.items[item_choice]["quantity"]
                        print(bcolors.OKBLUE, item.name, "fully restored your HP.", bcolors.ENDC)
                        print(bcolors.OKBLUE,"Left", item.name, ":", str(int(elixer_quantity)- 1) + "x" )
                    else :
                        print(bcolors.OKBLUE, "You have no ", item.name, ".", bcolors.ENDC)
                        continue

                if item.name == "MegaElixer" :
                    if player.items[item_choice]["quantity"] > 0:
                        for person in Players:
                            person.hp = person.maxhp
                        megaelixer_quantity = player.items[item_choice]["quantity"]
                        print(bcolors.OKBLUE, item.name, "fully restored the whole party HP/MP", bcolors.ENDC)
                        print(bcolors.OKBLUE,"Left", item.name, ":", str(int(megaelixer_quantity)- 1) + "x" )
                    else :
                        print(bcolors.OKBLUE, "You have no", item.name, ".", bcolors.ENDC)
                        continue


            elif item.type == "attack":
                if player.items[item_choice]["quantity"] > 0:
                    Enemies[player_target].take_damage(item.prop)
                    print(bcolors.FATL, "\n" , item.name, "damaged for " , str(item.prop), "points of HP.", bcolors.ENDC)
                    if Enemies[player_target].hp <= 0:
                        print(bcolors.FATL, Enemies[player_target].name , "has died." + bcolors.ENDC)
                        del Enemies[player_target]
                        Enemies_number -= 1
                        if Enemies_number == 0:
                            print("\n\n")
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            running = False
                        elif Players_number == 0:
                            print("\n\n")
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            running = False

                    attack_quantity = player.items[item_choice]["quantity"]
                    print(bcolors.OKBLUE,"Left", item.name, ":", str(int(attack_quantity)- 1) + "x" )
                else :
                    print(bcolors.OKGREEN, "You have no", item.name, ".", bcolors.ENDC)
                    continue


            player.items[item_choice]["quantity"] -= 1


        for enemy in Enemies:
            if Players_number <=0:
                break
            enemy_choice = 0                     #random.randrange(0, 2)

            if enemy_choice == 0:
                enemy_target = random.randrange(0 , Players_number)
                enemy_dmg = enemy.generate_damage()
                Players[enemy_target].take_damage(enemy_dmg)
                print("------------------------------------")
                print(bcolors.FATL,enemy.name , " attacks for " , enemy_dmg, "points of damage to",Players[enemy_target].name + ".",  bcolors.ENDC)

                if Players[enemy_target].hp <= 0:
                    print(bcolors.FATL, Players[enemy_target].name , "has died." + bcolors.ENDC)
                    del Players[enemy_target]
                    Players_number -= 1
                    if Enemies_number == 0:
                        print("\n\n")
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        running = False
                    elif Players_number == 0:
                        print("\n\n")
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
                        print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                        print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                        running = False


            elif enemy_choice == 1:
                spell_choice = enemy.enemy_choose_spell()


                if spell.type == "white":
                    enemy.take_heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + enemy.name, " healed its HP for " , str(magic_dmg), " points." + bcolors.ENDC)
                    if enemy.hp > enemy.maxhp:
                        enemy.hp = enemy.maxhp
                        print(enemy.name + "'s", "HP is now full.")

                elif spell.type == "black":
                    enemy_target = random.randrange(0 , Players_number)
                    Players[enemy_target].take_damage(magic_dmg)
                    print("\n"+ enemy.name, "chose", spell.name + ".")
                    print(bcolors.OKBLUE + spell.name, " damaged", Players[enemy_target].name, "for", str(magic_dmg), "points." + bcolors.ENDC)
                    if Players[enemy_target].hp <= 0:
                        print(bcolors.FATL, Players[enemy_target].name, "died." + bcolors.ENDC)
                        del Players[enemy_target]
                        Players_number -= 1
                        if Enemies_number == 0:
                            print("\n\n")
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            running = False
                        elif Players_number == 0:
                            print("\n\n")
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
                            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
                            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
                            running = False




    if running == True:
        if Enemies_number == 0:
            print("\n\n")
            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
            print(bcolors.OKGREEN + "...............Players Win.............." + bcolors.ENDC)
            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
            running = False

        elif Players_number == 0:
            print("\n\n")
            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
            print(bcolors.OKGREEN + ".............Players Defeats............." + bcolors.ENDC)
            print(bcolors.OKBLUE + "            *****************           " + bcolors.ENDC)
            print(bcolors.OKBLUE + "========================================" + bcolors.ENDC)
            running = False
            print( None )