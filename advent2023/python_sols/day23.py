import sys

sys.setrecursionlimit(10**6)

from collections import deque
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
grid = {}
mem = {}
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dir = {'>': (0,1), 'v': (1,0), '^': (-1,0), '<': (0,-1)}
print(len(data), len(data[0]))
def DFS(spot, vis, pre = (-1,-1)):
    print(spot)
    global grid, data, dx, dy, dir, mem
    if (spot) in mem:
        print(mem[spot]) 
        return mem[(spot)]
    ans = -10
    if spot == (len(data)-1, len(data[0])-2):
        return 0
    if spot in vis:
        return -10
    count = 0
    path = []
    for i in dir.values():
        new_spot = tuple(map(sum, zip(i, spot)))
        if (new_spot not in grid) or (grid[new_spot] == '#') or new_spot == pre or new_spot in vis:
            count+=1
        else:
            path.append(new_spot)
    if count == 3:
        vis.add(spot)
        ans = DFS(path[0], vis, spot)+1
        mem[(spot)] = ans
        vis.remove(spot)
        return ans

    else:
        vis.add(spot)
        for x in path:
            ans = max(ans, DFS(x, vis, spot))+1
        vis.remove(spot)
    print(count)
    mem[(spot)] = ans
    return ans


for r, line in enumerate(data):
    for c, ch in enumerate(line):
        grid[(r,c)] = ch

grid[(0,1)] = '#'
start = (1,1)
print(DFS(start, set()))
print(mem.values())
