# shortcut Ctrl + F2
import random as r


class Ship:
    def __init__(self, ship_name, ship_hp, ship_damage, ship_armour):
        self.ship_name = ship_name
        self.ship_hp = int(ship_hp)
        self.ship_damage = int(ship_damage)
        self.ship_armour = int(ship_armour)

    def attacks(self, attacked):
        # damage_dealt = abs(int(self.ship_damage * r.uniform(0, 1)) - attacked.ship_armour)
        damage_dealt = self.ship_damage - attacked.ship_armour

        if(damage_dealt < 0):
            damage_dealt = 1

        attacked.ship_hp -= damage_dealt

        if(attacked.ship_hp < 0):
            attacked.ship_hp = 0

        return damage_dealt

    def adds_upgrades(self, res_bool):
        '''
        adds upgrades to ships
        '''
        upgrades = {}
        k = 0
        with open("spaceships_upgrades.txt", "r") as file:
            for i in file.readlines():
                i = i.strip("\n").split(": ")
                upgrades[k+1] = i
                k += 1
        for k, i in upgrades.items():
            print(k, i)
        if (res_bool == False):
            choice = input("\nChoose an upgrade #: ")
            if (choice.isdecimal()):
                choice = upgrades[int(choice)]
                self.__calc_upgrade(choice)
            else:
                print("\nInvalid input. \nBattle still starts.")
        elif(res_bool == True):
            choice = upgrades[r.choice(range(1, len(upgrades) + 1))]
            print(f"\nComputer chose upgrade: {choice}")
            self.__calc_upgrade(choice)

    def __calc_upgrade(self, choice):
        if("Titanium armour" in choice):
            self.ship_hp += 250
            self.ship_armour += 3

        elif("Absorption shield" in choice):
            self.ship_armour = int(self.ship_armour * 1.5)

        elif("Proton torpedos" in choice):
            self.ship_damage += 25

        elif("Flare engine" in choice):
            self.ship_hp = int(self.ship_hp * 1.2)
            self.ship_damage = int(self.ship_damage * 1.5)
            self.ship_armour += 3

        elif("EMP cannon" in choice):
            self.ship_damage = int(self.ship_damage * 1.5)

        elif("Teleporting module" in choice):
            self.ship_armour = int(self.ship_armour * 1.25)

        elif("Molecular mirror" in choice):
            self.ship_armour = int(self.ship_armour * 1.10)

        else:
            print("Upgrade not found.")


class Game:
    def __init__(self):
        self.ON = True
        # self.OFF = False
        self.player = object
        self.computer = object
        self.steps = 0
        self.DEAD = 0

    def start(self, _start):
        if(_start):
            spaceships = []
            with open('spaceships.txt', 'r') as file:
                for i in file.readlines():
                    i = i.strip("\n").split(", ")
                    spaceships.append(i)

            '''computer'''
            self.computer = Ship(*r.choice(spaceships))

            '''versus'''

            '''player'''
            self.player = Ship(*r.choice(spaceships))

            '''decides for upgrades'''
            if(r.choice([True, False]) == True):
                self.computer.adds_upgrades(True)
            if(input("\nWould you like to have upgrades? [Y/N]: ").lower() == "y"):
                self.player.adds_upgrades(False)

            self.__display_versus(self.computer, self.player)
            self.run_game()

    def run_game(self):
        attacker = r.choice([self.computer, self.player])
        while (self.computer.ship_hp and self.player.ship_hp > self.DEAD):
            self.__print_separator()
            if(attacker == self.computer):
                damage_dealt = attacker.attacks(self.player)
                self.__print_fight(attacker, self.player, damage_dealt)
                attacker = self.player
            else:
                damage_dealt = attacker.attacks(self.computer)
                self.__print_fight(attacker, self.computer, damage_dealt)
                attacker = self.computer
        else:
            self.__display_winner()

    def __display_versus(self, computer, player):
        print(f"\n\nYou are: {player.ship_name}\n" +
              f"HP = {player.ship_hp}\n" +
              f"Damage points = {player.ship_damage}\n" +
              f"Armour points = {player.ship_armour}")

        print("\nVERSUS\n")

        print(f"Your enemy is: {computer.ship_name}\n" +
              f"HP = {computer.ship_hp}\n" +
              f"Damage points = {computer.ship_damage}\n" +
              f"Armour points = {computer.ship_armour}\n\n")

    def __print_separator(self):
        print("-" * 50, f"\nStep {self.steps + 1}")
        self.steps += 1

    def __print_fight(self, attacker, attacked, damage_dealt):
        print(f"{attacker.ship_name} attacks {attacked.ship_name} with {attacker.ship_damage} attack damage. \n{damage_dealt} damage dealt to {attacked.ship_name}'s {attacked.ship_armour} armour. \n{attacked.ship_name} HP left: {attacked.ship_hp}")

    def __display_winner(self):
        if(self.player.ship_hp <= 0):
            print(f"Computer's {self.computer.ship_name} won!\n" +
                  f"Your ship {self.player.ship_name} was destroyed.")
        else:
            print(f"Your ship {self.player.ship_name} won!\n" +
                  f"Computer's ship {self.computer.ship_name} was destroyed.")


if __name__ == "__main__":
    battle = Game()
    battle.start(battle.ON)
