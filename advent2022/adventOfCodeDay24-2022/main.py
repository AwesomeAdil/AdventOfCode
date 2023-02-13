import collections
raw = open('sample.txt', 'r').read().split('\n')
grid = [list(row) for row in raw]
blizzards = set()
blocked = set()
move = [(1,0), (-1, 0), (0, 1), (0, -1)]
directions = ['v', '^', '>', '<']
move_blizzards = {key: val for key, val in zip(directions, move)}
dir = {key: val for val, key in move_blizzards.items()}
res = 0

def update_blizzard():
    global blizzards
    global blocked
    temp_blocked = set()
    temp = set()
    for blizzard in blizzards:
        nx = ((blizzard[0][0] + blizzard[1][0] - 1) % (len(grid) - 2)) + 1
        ny = ((blizzard[0][1] + blizzard[1][1] - 1) % (len(grid[0]) - 2)) + 1
        temp.add((blizzard[0], (nx, ny)))
        temp_blocked.add((nx, ny))
    blizzards = temp
    blocked = temp_blocked
    for i in range(len(grid)):
        blocked.add((i, 0))
        blocked.add((i, len(grid[0]) - 1))
    for i in range(len(grid[0])):
        blocked.add((0, i))
        blocked.add((len(grid) - 1, i))

    blocked.remove((0, 1))
    blocked.remove((len(grid) - 1, len(grid[0]) - 2))


for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val != '.' and val != '#':
            blizzards.add((move_blizzards[val], (i, j)))
            blocked.add((i, j))
        elif val != '.':
            blocked.add((i, j))

q = collections.deque()

q.append((0, (0, 1)))
visited = set()
old_time = -1
#update_blizzard()
while q:
    time, loc = q.popleft()
    if (time, loc) in visited:
        continue

    visited.add((time, loc))
    if time > old_time:
        update_blizzard()
        old_time = time

    if loc == (len(grid) - 1, len(grid[0]) - 2):
        res += time
        print('Part 1:', time)
        q.clear()
        q.append((0, (loc)))
        break


    if loc not in blocked:
        q.append((time+1, loc))

    for dx, dy in move:
        nx, ny = loc[0] + dx, loc[1] + dy

        if (nx, ny) not in blocked and nx >= 0:
            q.append((time+1, (nx, ny)))

old_time = 0
time = 0
visited.clear()
while q:
    time, loc = q.popleft()
    if (time, loc) in visited:
        continue

    visited.add((time, loc))
    if time > old_time:
        update_blizzard()
        old_time = time

    if loc == (0, 1):
        res += time
        print(time)
        q.clear()
        q.append((0, (loc)))
        break

    if loc not in blocked:
        q.append((time + 1, loc))

    for dx, dy in move:
        nx, ny = loc[0] + dx, loc[1] + dy

        if (nx, ny) not in blocked and nx < len(grid) - 1:
            q.append((time + 1, (nx, ny)))

old_time = 0
time = 0
visited.clear()
while q:
    time, loc = q.popleft()
    if (time, loc) in visited:
        continue

    visited.add((time, loc))
    if time > old_time:
        update_blizzard()
        old_time = time

    if loc == (len(grid) - 1, len(grid[0]) - 2):
        res+=time
        print(time)
        q.clear()
        q.append((0, (loc)))
        break


    if loc not in blocked:
        q.append((time+1, loc))

    for dx, dy in move:
        nx, ny = loc[0] + dx, loc[1] + dy

        if (nx, ny) not in blocked and nx >= 0:
            q.append((time+1, (nx, ny)))

print('Part 2:', res)