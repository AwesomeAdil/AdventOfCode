from aocd import get_data
data = get_data(day=14, year=2022).split('\n')

sand = 0
rocks = set()
maxDepth = 0
for line in data:
    pairs = line.split(' -> ')
    for x in range(1, len(pairs)):
        nx, ny = map(int, pairs[x].split(','))
        ox, oy = map(int, pairs[x-1].split(','))
        dx, dy = nx - ox, ny - oy

        maxDepth = max(maxDepth, ny, oy)
        for i in range(max(abs(dx), abs(dy)) + 1):
            cx = ox + (1 if dx > 0 else -1 if dx < 0 else 0) * i
            cy = oy + (1 if dy > 0 else -1 if dy < 0 else 0) * i
            rocks.add((cx, cy))


falling = True
for x in range(-5000, 5000):
    rocks.add((x, maxDepth+2))
while falling:
    sx, sy = 500, 0
    blocked = False
    while not blocked:
        if (sx, sy+1) not in rocks:
            sy += 1
        elif (sx-1, sy+1) not in rocks:
            sx -= 1
            sy += 1
        elif (sx+1, sy+1) not in rocks:
            sx += 1
            sy += 1
        else:
            blocked = True
    if blocked:

        if (sx, sy) in rocks:
            break
        sand += 1
        rocks.add((sx, sy))

print(sand)