import sys
sys.setrecursionlimit(10**6)
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

row = len(data)
col = len(data[0])
grid = {}
energized = set()
seen = set()
cur = (0, 0)
dir = (0, 1)

for i in range(row):
    for j in range(col):
        grid[(i,j)] = data[i][j]

def addd(x, y):
    return (x[0]+y[0], x[1]+y[1])

def subb(x,y):
    return (x[0]-y[0], x[1]-y[1])

count = 0
def move(spot, dir):
    spot = addd(spot, dir)
    global seen, energized, grid, count
    if (spot, dir) in seen:
        return
    if spot[0]>=row or spot[1] >= col or spot[0] < 0 or spot[1] < 0:
        return
    seen.add((spot, dir))
    energized.add(spot)
    if grid[spot] == '/':
        if dir == (1,0):
            move(spot, (0,-1))
        elif dir == (0,-1):
            move(spot, (1,0))
        elif dir == (0, 1):
            move(spot, (-1, 0))
        else:
            move(spot, (0, 1))
    elif grid[spot] == '\\':
        if dir == (1,0):
            move(spot, (0,1))
        elif dir == (0,-1):
            move(spot, (-1,0))
        elif dir == (0, 1):
            move(spot, (1, 0))
        else:
            move(spot, (0, -1))
    elif grid[spot] == '-' and dir in [(1,0), (-1, 0)]:
        move(spot, (0,1))
        move(spot, (0,-1))
    elif grid[spot] == '|' and dir in [(0,1), (0,-1)]:
        move(spot, (1,0))
        move(spot, (-1,0))
    else:
        move(spot, dir)

ans = -1
for index, dir in enumerate([(1,0), (-1,0), (0,1), (0,-1)]):
    for i in range(row):
        seen.clear()
        energized.clear()
        if index == 0:
            move(subb((0,i), dir), dir)
        elif index == 1:
            move(subb((row-1,i), dir), dir)
        elif index == 2:
            move(subb((i,0), dir), dir)
        else:
            move(subb((i,col-1), dir), dir)
        ans = max(ans, len(energized))
print(ans)
