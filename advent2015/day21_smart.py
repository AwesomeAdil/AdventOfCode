min_cost = {} # tells the min cost for certain attack and defense
max_cost = {} # tells max cost for certain attack and defense
wins = {} # tells if certain attack defense wins against the boss


boss_health = 100
boss_damage = 8
boss_armor = 2

for i in range(20):
    for j in range(20):
        wins[(i, j)] = math.ceil(100 / max(i - boss_armor, 1)) <= math.ceil(100 / max(boss_damage - j, 1))
        

min_cost[(0,0)] = 0
max_cost[(0,0)] = 0


