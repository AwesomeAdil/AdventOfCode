raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def gdc(a,b):
    return a if b == 0 else gdc(b, a%b)

def lcml(x):
    if len(x) == 0:
        return 1
    if len(x) == 1:
        return x[0]
    if len(x) == 2:
        return lcm(x[0], x[1])
    return lcm(lcml(x[:len(x)//2]), lcml(x[len(x)//2:]))

def lcm(a,b):
    return (a*b)//gdc(a,b)

paths = {}
points = []
for line in data[2:]:
    parts = line.split(' = ')
    b,c =  parts[-1].split(',')
    if parts[0][-1] == 'A':
        points.append(parts[0])
    paths[parts[0]] = (b[1:], c[1:-1])


"""    
steps = 0
point = "AAA"
while point != "ZZZ":
    x = 0 if data[0][steps%len(data[0])] == "L" else 1
    point = paths[point][x]
    steps+=1

print(steps) 
"""

steps = 0
org = []
seen = []
zs = {}
rots = {}
pos = {}
first_time = {}
for x in points:
    org.append(x)
    seen.append(False)
    pos[x] = []
    first_time[x] = {}

init = {}
loops = {}
while False in seen:
    new_points = []
    y = 0 if data[0][steps%len(data[0])] == "L" else 1
    for i, x in enumerate(points):
        if not seen[i]:
            if steps!=0 and (paths[x][y], steps%len(data[0])) in pos[org[i]]:
                seen[i] = True
                rots[org[i]] = steps
                init[org[i]] = zs[org[i]][0] #first_time[org[i]][(paths[x][y], steps%len(data[0]))]
                loops[org[i]] = steps - first_time[org[i]][(paths[x][y], steps%len(data[0]))] 
            else:
                if paths[x][y][-1] == "Z":
                    if org[i] not in zs:
                        zs[org[i]] = []
                    zs[org[i]].append(steps+1)
        new_points.append(paths[x][y])
        pos[org[i]].append((paths[x][y], steps%len(data[0])))
        first_time[org[i]][(paths[x][y], steps%len(data[0]))] = steps

    points = new_points
    steps+=1

#things = []
#rotations = []
#for x, r in zip(zs.values(), rots.values()):
#    things.append([x,r])
vals = []
for i in org:
    vals.append(init[i])

print(lcml(vals))

## turned out numbers get really nice for an LCM
