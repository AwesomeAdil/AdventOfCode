from aocd import get_data

data = get_data(day=18, year=2022).split('\n')
cubes = {}
move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
visited = {}


def canReach(x, y, z):
    if (x, y, z) in visited:
        return visited[(x, y, z)]
    if abs(x) >= 20 or abs(y) >= 20 or abs(z) >= 20:
        return True

    visited[(x, y, z)] = False
    for dx, dy, dz in move:
        if (x + dx, y + dy, z + dz) not in cubes:
            visited[(x, y, z)] = canReach(x + dx, y + dy, z + dz)
            if visited[(x, y, z)]:
                return True

    return visited[(x, y, z)]


for line in data:
    x, y, z = eval(line)
    cubes[(x, y, z)] = 1

count = 0
for x, y, z in cubes:
    for dx, dy, dz in move:
        if (x + dx, y + dy, z + dz) not in cubes:
            count += 1

print("Part 1:", count)

count = 0
for x, y, z in cubes:
    for dx, dy, dz in move:
        if (x + dx, y + dy, z + dz) not in cubes:
            count += (1 if canReach(x + dx, y + dy, z + dz) else 0)

print("Part 2:", count)
