from aocd import get_data
raw = open('sample.txt', 'r').read().split('\n')
data = list(list(line) for line in raw)
elfs = set()
bounds = [1e9, -1e9, 1e9, -1e9] # min_x, max_x, min_y, max_y


def check_north(x, y):
    for i in range(-1, 2):
        if (x-1, y+i) in elfs:
            return False
    return True

def check_south(x, y):
    for i in range(-1, 2):
        if (x+1, y+i) in elfs:
            return False
    return True

def check_west(x, y):
    for i in range(-1, 2):
        if (x + i, y - 1) in elfs:
            return False
    return True

def check_east(x, y):
    for i in range(-1, 2):
        if (x + i, y + 1) in elfs:
            return False
    return True

def check_alone(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if (x+i, y+j) in elfs:
                return False
    return True


def printGrid():
    for i in range(bounds[0], bounds[1] + 1):
        for j in range(bounds[2], bounds[3] + 1):
            if (i, j) in elfs:
                print(end='#')
            else:
                print(end='.')

        print()

consider = [(check_north, (-1, 0)), (check_south, (1, 0)), (check_west, (0, -1)), (check_east, (0, 1))]

def update_bounds(x, y):
    global bounds
    bounds[0] = min(bounds[0], x)
    bounds[1] = max(bounds[1], x)
    bounds[2] = min(bounds[2], y)
    bounds[3] = max(bounds[3], y)


for i, row in enumerate(data):
    for j, val in enumerate(row):
        if val == '#':
            elfs.add((i,j))
            update_bounds(i, j)

round = 0
found = False
while not found:
    round += 1
    found = True
    new_spots = {}
    dup_spots = set()
    new_elfs = set()
    # Step one
    for elf in elfs:
        if check_alone(elf[0], elf[1]):
            new_spots[elf] = elf
            continue
        for index, check in enumerate(consider):
            if check[0](elf[0], elf[1]):
                nx, ny = list(a + da for a, da in zip(elf, check[1]))
                if (nx, ny) in dup_spots:
                    new_spots[elf] = elf
                elif (nx, ny) in new_spots.values():
                    new_spots[elf] = elf
                    dup_spots.add((nx, ny))
                else:
                    new_spots[elf] = (nx, ny)
                break
            else:
                new_spots[elf] = elf
    # Step two
    consider.append(consider.pop(0))
    for elf, ns in new_spots.items():
        if ns in dup_spots:
            new_elfs.add(elf)
            update_bounds(elf[0], elf[1])
        else:
            if elf != ns:
                found = False
            new_elfs.add(ns)
            update_bounds(ns[0], ns[1])

    elfs = new_elfs


print(round)
print((bounds[1] -bounds[0] + 1) * (bounds[3] - bounds[2] + 1) - len(elfs))