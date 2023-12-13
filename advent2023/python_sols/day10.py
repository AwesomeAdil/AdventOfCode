from collections import defaultdict 
import sys
sys.setrecursionlimit(10000000)

directions = {'|' : [(1, 0), (-1,0)], '-' : [(0, 1), (0, -1)], 'L' : [(-1, 0), (0, 1)],
              'J' : [(-1, 0), (0, -1)], '7': [(1, 0), (0, -1)], 'F': [(1,0), (0, 1)], 
              'S' : [(1,0), (-1,0), (0,1), (0,-1)], '.': [], '*':[]}

def def_value1(): 
    return -1

def def_value2():
    return '*'

d = defaultdict(def_value1)
grid = defaultdict(def_value2)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maxer = -1

loop_edges = set()
def findDists(x, y, dist, prev):
    global maxer, d, grid, loop_edges
    if grid[(x, y)] == 'S' and dist != 0:
        spot_x, spot_y = prev[0], prev[1]
        p = (x, y)
        count = 0
        while grid[(spot_x, spot_y)] != 'S':
            count += 1
            loop_edges.add((spot_x, spot_y))
            for dir in directions[grid[(spot_x, spot_y)]]:
                nx = spot_x+dir[0]
                ny = spot_y+dir[1]
                if (nx, ny) != p:
                    p = (spot_x, spot_y)
                    spot_x, spot_y = nx, ny
                    break
        loop_edges.add((x, y))

    if d[(x,y)] != -1 and d[(x, y)] < dist:
        return 
    
    if grid[(x, y)] == '.' or grid[(x, y)]=='*':
        return -1
    
    d[(x, y)] = dist
    val = dist
    for dir in directions[grid[(x, y)]]:
        nx = x+dir[0]
        ny = y+dir[1]
        flipped = (dir[0]*-1, dir[1] * -1)
        if not (nx == prev[0] and ny == prev[1]) and flipped in directions[grid[(nx, ny)]]:
            findDists(nx, ny, val+1, (x, y))

seen = {}
amts = {}
doesnt_work = set()

raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')

start = (-1, -1)
for r, line in enumerate(data):
    for c, ch in enumerate(line):
        grid[(r,c)] = ch
        if ch == 'S':
            d[(r,c)] = 0
            start = (r,c)

findDists(start[0], start[1], 0, (-1, -1))

ans = 0
grid[start] = '-'
for r, line in enumerate(data):
    num_edges = 0
    edge = 'n'
    for c, ch in enumerate(line):
        if (r,c) in loop_edges and grid[(r,c)] == '|':
           num_edges = (num_edges+1)%2
        elif (r,c) in loop_edges and grid[(r,c)] in ['L', 'F']:
            edge = grid[(r,c)]
        elif (r,c) in loop_edges and grid[(r,c)] in ['7','J']:
            if (edge == 'L' and grid[(r,c)] == '7') or (edge =='F' and grid[(r,c)] == 'J'):
                num_edges = (num_edges+1)
        elif num_edges == 1 and (r,c) not in loop_edges:
            ans += 1

print("HERE",  ans)
print(max(d.values()))
