import subprocess

boss_health = 71
boss_attack = 10
health = 50
mana = 500

class Scenario:
    roof = 10000000
    def __init__(self, boss_health, boss_attack, mana, health, effects, mana_spent, steps):
        self.boss_health = boss_health
        self.boss_attack = boss_attack
        self.mana = mana
        self.health = health
        self.effects = effects
        self.mana_spent = mana_spent
        self.steps = steps


    def Magic_Missle(self):
        self.mana -= 53
        self.mana_spent += 53
        self.boss_health -= 4

    def Drain(self):
        self.mana -= 73
        self.mana_spent += 73
        self.boss_health -= 2
        self.health += 2

    def Shield(self):
        self.mana -= 113
        self.mana_spent += 113
        self.effects['sd'] = 6

    def Poison(self):
        self.mana -= 173
        self.mana_spent += 173
        self.effects['pn'] = 6

    def Recharge(self):
        self.mana -= 229
        self.mana_spent += 229
        self.effects['re'] = 5

    # Define the less-than comparison for the class
    def __lt__(self, other):
        return self.mana_spent < other.mana_spent

    moves = {"Magic Missle": Magic_Missle,
             "Drain": Drain,
             "Shield": Shield,
             "Poison": Poison,
             "Recharge":Recharge}


    def Passives(self):
        if self.effects['pn'] > 0:
            self.boss_health -= 3
            self.effects['pn'] -= 1

        if self.effects['re'] > 0:
            self.mana += 101
            self.effects['re'] -= 1

        if self.effects['sd'] > 0:
            self.effects['sd'] -=1

    def getAttacked(self):
        if self.effects['sd'] > 0:
            self.health -= max(self.boss_attack - 7, 1)
        else:
            self.health -= self.boss_attack
    def checkWin(self):
        if self.boss_health <= 0:
            return 1
        elif self.health <= 0:
            return -1
        return 0

    def hardmode(self):
        self.health -= 1
    
    def makeCopy(self):
        return Scenario(self.boss_health, self.boss_attack, self.mana, self.health, self.effects.copy(), self.mana_spent, self.steps.copy())

    def makeMove(self):
        inp = input("Make a move: ")

    def display(self):
        subprocess.run('clear', shell=True)
        print('boss_health:', self.boss_health, 'health:', self.health, 'mana', self.mana, 'spent', self.mana_spent)



    def game(self):
        hardmode_on = input("hardmode? ('y/N)")
        hardmode_on = hardmode.lower() == 'y'  
        while True:
            if hardmode_on:
                self.hardmode()
            inp = "NA"
            while inp not in moves:
                inp = input("Make a move: ")



sen = Scenario(boss_health, boss_attack, mana, health, {'sd': 0, 'pn': 0, 're': 0}, 0, [])


