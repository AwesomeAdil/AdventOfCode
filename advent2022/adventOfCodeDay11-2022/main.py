from aocd import get_data
data = get_data(day=11, year=2022).split('\n')


def lcm(c):
    prod = 1
    for x in c:
        prod *= x
    return prod


monkey = []
ops = []
tests = []
to_monkey = []
inspected = []
big_d = -1


def monkeyTurn(i):
    while len(monkey[i]):
        a = int(ops[i][0]) if ops[i][0].isnumeric() else monkey[i][0]
        b = int(ops[i][-1]) if ops[i][-1].isnumeric() else monkey[i][0]
        newWorry = (a + b) if ops[i][1] == '+' else newWorry = (a * b)
        if newWorry % tests[i] == 0:
            monkey[to_monkey[i][0]].append(newWorry % big_d)
        else:
            monkey[to_monkey[i][1]].append(newWorry % big_d)
        monkey[i].pop(0)
        inspected[i] += 1


def do_round():
    for i in range(len(monkey)):
        monkeyTurn(i)


for x in range(0, len(data), 7):
    monkey.append(list(map(lambda y: int(y.strip()), (data[x + 1].split(':'))[-1].split(','))))
    ops.append(data[x + 2].split()[-3:])
    tests.append(int(data[x + 3].split()[-1]))
    options = [int(data[x + 4].split()[-1]), int(data[x + 5].split()[-1])]
    to_monkey.append(tuple(options))
    inspected.append(0)

big_d = lcm(tests)
for _ in range(10000):
    do_round()

print(sorted(inspected)[-1] * sorted(inspected)[-2])
