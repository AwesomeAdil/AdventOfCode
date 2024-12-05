import heapq

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

    def recurse(self):
        #print(self.boss_health, self.health, self.mana_spent, self.mana)
        self.Passives()
        res = self.checkWin()
        if res == 1:
            return self.mana_spent
        if res == -1:
            return 10000000

        ans = 10000000
        for type, move in self.moves.items():
            newScenario = self.makeCopy()
            newScenario.steps.append(type)
            works = True
            if type == 'Shield' and newScenario.effects['sd'] > 0:
                continue
            if type == 'Poison' and newScenario.effects['pn'] > 0:
                continue
            if type == 'Recharge' and newScenario.effects['re'] > 0:
                continue
            move(newScenario)
            newScenario.Passives()
            newScenario.getAttacked()
            res = newScenario.checkWin()
            if res == 1:
                ans = min(newScenario.mana_spent, ans)
            elif res == 0:
                ans = min(ans, newScenario.recurse())
            self.roof = min(self.roof, ans)
        return ans
    """
    def fromOrigin(self, boss_health, boss_attack, mana, health):
        cur = Scenario(boss_health, boss_health, mana, health, {'sd': 0, 'pn': 0, 're': 0}, 0, [])
        for step in self.steps:
            print('boss_health:', cur.boss_health, 'health:', cur.health, 'mana', cur.mana, 'spent', cur.mana_spent)
            print('MOVE:', step)
            cur.moves[step](cur)
        print('boss_health:', cur.boss_health, 'health:', cur.health, 'mana', cur.mana, 'spent', cur.mana_spent)
    """



sen = Scenario(boss_health, boss_attack, mana, health, {'sd': 0, 'pn': 0, 're': 0}, 0, [])
#print(sen.recurse())
def Dijkstra():
    pq = []
    heapq.heappush(pq, sen)
    roof = 10000000
    while pq:
        top = heapq.heappop(pq)
        if top.mana_spent > top.roof:
            continue 
    
        top.hardmode()
        res = top.checkWin()
        if res == 1:
            print('ANS:', top.mana_spent, top.steps)
            return top
            break
        if res == -1:
            continue

        top.Passives()
        res = top.checkWin()
        if res == 1:
            print('ANS:', top.mana_spent, top.steps)
            return top
            break
        if res == -1:
            continue
    
        for type, move in top.moves.items():
            newScenario = top.makeCopy()
            newScenario.steps.append(type)
            works = True
            if type == 'Shield' and newScenario.effects['sd'] > 0:
                continue
            if type == 'Poison' and newScenario.effects['pn'] > 0:
                continue
            if type == 'Recharge' and newScenario.effects['re'] > 0:
                continue
    
            move(newScenario)
            if newScenario.mana < 0:
                continue
            newScenario.Passives()
            res = newScenario.checkWin()
            if res == -1:
                continue
            newScenario.getAttacked()
            res = newScenario.checkWin()
            if res == -1:
                continue
            heapq.heappush(pq, newScenario)
ans = Dijkstra()

ans.fromOrigin(boss_health, boss_attack, mana, health)
