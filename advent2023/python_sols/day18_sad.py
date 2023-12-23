raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def shoe(x):
    U = 0
    L = 0
    for i in range(len(x)-1):
        L += x[i-1][0]*x[i][1]
        U += x[i-1][1]*x[i][0]
    return abs(U-L)/2

def invpick(x, b):
    # A = i + b/2 - 1 -> i + b = A + b/2 + 1
    A = shoe(x)
    return A + b/2 + 1


cur = (0, 0)
dirs = {'R': (0,1), 'D':(1,0), 'U': (-1, 0), 'L': (0,-1)}
dir_x = {'0': 'R', '1': 'D', '2':'L', '3': 'U'}
points = [(0,0)]
perim = 0
for line in data:
    parts = line.split()
    imp = parts[-1][1:-1]
    dir = dirs[dir_x[imp[-1]]]
    dist = int(imp[1:-1], 16)
    perim += dist
    cur = (cur[0] + dir[0] * dist, cur[1] + dir[1] * dist)
    #perim += int(parts[1])
    #cur = (cur[0] + dirs[parts[0]][0] * int(parts[1]), cur[1] + dirs[parts[0]][1] * int(parts[1]))
    points.append(cur)
print(perim)

print(invpick(points, perim))



