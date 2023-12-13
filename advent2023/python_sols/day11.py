raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
galaxy_x = set()
galaxy_y = set()
dx = [0]
dy = [0]
def calcDist(x, y):
    global dx, dy
    return dx[max(x[0], y[0])] - dx[min(x[0], y[0])] + dy[max(x[1], y[1])] - dy[min(x[1], y[1])]

galaxies = []
grid = {}

for r, line in enumerate(data):
    for c, ch in enumerate(line):
        if ch == '#':
            galaxies.append((r,c))
            galaxy_x.add(r)
            galaxy_y.add(c)

for i in range(len(data)):
    dx.append(dx[-1] + (1000000 if i not in galaxy_x else 1))

for i in range(len(data)):
    dy.append(dy[-1] + (1000000 if i not in galaxy_y else 1))

ans = 0
count = 0
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        ans += calcDist(galaxies[i], galaxies[j])
        count+=1
print(ans)
