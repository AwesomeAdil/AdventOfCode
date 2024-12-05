import math
class Player:
    expense = 0
    build = []
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def turns_survive(self, damage):
        return math.ceil ((self.health)/max(damage - self.armor, 1))

    def beats(self, other):
        return other.turns_survive(self.damage) <= self.turns_survive(other.damage)

    def addItem(self, item):
        self.damage += item.damage
        self.armor += item.armor
        self.expense += item.cost
        self.build.append(item.name)

    def removeItem(self, item):
        self.damage -= item.damage
        self.armor -= item.armor
        self.expense -= item.cost
        self.build.remove(item.name)
    def getCost(self):
        return self.expense

    def getBuild(self):
        return self.build

class Item:
    def __init__(self, name, damage, armor, cost):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.cost = cost

weapons = [Item('Dagger', 4, 0 , 8), Item('Shortsword', 5, 0 ,10), Item('Warhammer', 6, 0 ,25), Item('Longsword', 7, 0 , 40), Item('Greataxe', 8, 0, 74)]
armors = [Item('No Armor', 0, 0, 0), Item('Leather', 0, 1, 13), Item('Chainmail', 0, 2, 31), Item('Splintmail', 0, 3, 53), Item('Bandedmail', 0,4,75), Item('Platemail', 0, 5, 102)]
rings = [Item('No Ring', 0, 0, 0), Item('No Ring', 0,0,0), Item('Damage +1', 1, 0, 25), Item('Damage + 2', 2, 0, 50), Item('Damage + 3', 3, 0, 100), Item('Defense + 1', 0, 1, 20), Item('Defense + 2', 0, 2, 40), Item('Defense + 3', 0, 3, 80)]

boss = Player(100, 8, 2)
hero = Player(100, 0, 0)

min_to_win = 100000
max_to_lose = 0
min_build = []
max_build = []
for weapon in weapons:
    hero.addItem(weapon)
    for armor in armors:
        hero.addItem(armor)
        for i, ring1 in enumerate(rings):
            for ring2 in rings[i+1:]:
                hero.addItem(ring1)
                hero.addItem(ring2)
                if hero.beats(boss):
                    if min_to_win > hero.getCost():
                        min_to_win = hero.getCost()
                        min_build = [x for x in hero.getBuild()]
                else:
                    if max_to_lose < hero.getCost():
                        max_to_lose = hero.getCost()
                        max_build = [x for x in hero.getBuild()]
                hero.removeItem(ring1)
                hero.removeItem(ring2)
        hero.removeItem(armor)
    hero.removeItem(weapon)
print(min_to_win, max_to_lose)
print(min_build)
print(max_build)

