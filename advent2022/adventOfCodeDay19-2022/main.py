from math import ceil
from aocd import get_data

data = get_data(day=19, year=2022).split('\n')
#data = open('sample.txt', 'r').read().split('\n')

quality = []
blueprints = []
dp = {}
change = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
max_mats = []

def qual(group, time):
    dp.clear()
    robots = (1, 0, 0, 0)
    mats = (0, 0, 0, 0)
    return recurse(robots, mats, time, group)


def recurse(robots, mats, time, info):
    if time <= 0:
        return mats[-1]
    if (robots, mats, time) in dp:
        return dp[(robots, mats, time)]
    best_choice = 0

    #
    # for i in range(3):
    #     if mats[i] < info[3][i]:
    #         break
    # else:
    #     new_mats = tuple(mats - price for mats, price in zip(mats, info[3]))
    #     new_mats = tuple(robot + mat for robot, mat in zip(robots, new_mats))
    #     new_robots = tuple(robot + dr for robot, dr in zip(robots, change[3]))
    #     best_choice = max(best_choice, recurse(new_robots, new_mats, time - 1, info))
    #     dp[(robots, mats, time)] = best_choice
    #     return best_choice

    for i in range(4):
        works = True
        amt_time = 1
        if i < 3 and robots[i] > max_mats[i]:
            works = False
        for j in range(3):
            if mats[j] < info[i][j] and robots[j] == 0:
                works = False
                break
            elif mats[j] < info[i][j]:
                amt_time = max(amt_time, ceil((info[i][j] - mats[j]) / robots[j]) + 1)
                if amt_time > time:
                    works = False
                    break

        if works:
            new_mats = tuple(mats - price for mats, price in zip(mats, info[i]))
            new_mats = tuple(robot * (amt_time) + mat for robot, mat in zip(robots, new_mats))
            new_robots = tuple(robot + dr for robot, dr in zip(robots, change[i]))
            best_choice = max(best_choice, recurse(new_robots, new_mats, time - amt_time, info))

        if best_choice == 0:
            best_choice = max(best_choice, robots[-1] * time + mats[-1])

    dp[(robots, mats, time)] = best_choice
    return best_choice


for line in data:
    x = line.split()
    ore = (int(x[6]), 0, 0, 0)  # ore
    clay = (int(x[12]), 0, 0, 0)  # ore
    obsidian = (int(x[18]), int(x[21]), 0, 0)  # ore and clay
    geode = (int(x[27]), 0, int(x[30]), 0)  # ore and obsidian
    max_mats = tuple(max(a, b, c, d) for a, b, c, d in zip(ore, clay, obsidian, geode))
    blueprints.append((ore, clay, obsidian, geode))


for index, blueprint in enumerate(blueprints[:3], 1):
    quality.append(qual(blueprint, 32))

prod = 1
for val in quality:
    prod *= val

print(prod)
