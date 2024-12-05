import matplotlib.pyplot as plt
import numpy as np
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


reachable[0] = set([start])
evens = set([start])
odds = set()

unseen = set()
ans = [1]
for i in range(2*131+66):
    reachable[i+1] = set()
    for element in reachable[i]:
        for x, y in zip(dx, dy):
            nx, ny = element[0] + x, element[1] + y

            #if 0<=nx<rows and 0<=ny<cols
            if grid[(nx%len(data), ny%len(data[0]))] != '#':
                reachable[i+1].add((nx, ny))
    ans.append(len(reachable[i+1]))
print(len(reachable[65]), len(reachable[131 +65]), len(reachable[2*131+65]))
print(len(reachable[64]))
x = np.array([0.0, 1.0, 2.0])
y = np.array([len(reachable[65]), len(reachable[131 +65]), len(reachable[2*131+65])])
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
print(p(202300))
