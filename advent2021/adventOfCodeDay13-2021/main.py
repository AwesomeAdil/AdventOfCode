from aocd import get_data
data = get_data(day=13, year = 2021).split('\n')
locs = set()
folds = False
start = 0

for index, line in enumerate(data):
    if line == '':
        start = index+1
        break
    locs.add(tuple(map(int, line.split(','))))


for line in data[start:]:
    fold = line.split()[-1]
    axis, spot = fold.split('=')
    spot = int(spot)
    updater = set()

    for spots in locs:
        x, y = spots
        if axis == 'x' and x > spot:
            updater.add((2 * spot - x, y))
        elif axis == 'y' and y > spot:
            updater.add((x, 2 * spot - y))
        else:
            updater.add((x, y))

    locs = updater

for j in range(7):
    for i in range(40):
        if (i, j) not in locs:
            print(end=' ')
        else:
            print(end='*')
    print()

print(len(locs))