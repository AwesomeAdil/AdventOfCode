raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]


reachable = {}

start = (0,0)
grid = {}
dx = [1, -1, 0, 0]
dy = [0,0,1,-1]
rows = len(data)
cols = len(data[0])
for r, line in enumerate(data):
    for c, ch in enumerate(line):
        if ch == 'S':
            start = (r,c)
        grid[(r,c)] = ch


reachable[0] = set()
evens = set()
odds = set()

unseen = set([start])
"""
for i in range(64):
    reachable[i+1] = set()
    for element in reachable[i]:
        for x, y in zip(dx, dy):
            nx, ny = element[0] + x, element[1] + y
            if 0<=nx<rows and 0<=ny<cols and grid[(nx, ny)] != '#':
                reachable[i+1].add((nx, ny))
"""      
for i in range(26501365 + 1):
    print(i)
    adder = set()
    for element in unseen:
        for x, y in zip(dx, dy):
            nx, ny = element[0] + x, element[1] + y
            if (nx, ny) in evens or (nx, ny) in odds:
                continue
            if grid[(nx%rows, ny%cols)] == '#':
                continue
            adder.add((nx, ny))
            if i == 1:
                odds.add((nx, ny))
            else:
                evens.add((nx, ny))
    unseen = adder


print(len(odds))
