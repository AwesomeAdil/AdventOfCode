raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def merge(x):
    if len(x) <= 1:
        return x
    while len(x)>1 and x[0][1] >= x[1][0]:
        x = [(min(x[0][0],x[1][0]), max(x[0][1],x[1][1]))] + x[2:]
    return [x[0]] + merge(x[1:])

def roofed(a,b):
    #print(a)
    s = 0
    for interval in b:
        if a[1]<interval[0]:
             break
        overlap_start = max(interval[0], a[0])
        overlap_end = min(interval[1], a[1])
        
        if overlap_start <= overlap_end:
            s+= overlap_end - overlap_start + 1
    return s

cur = (0, 0)
spots = {}
min_y = 0
max_y = 0
dirs = {'R': (0,1), 'D':(1,0), 'U': (-1, 0), 'L': (0,-1)}
points = set()
points.add(cur)
s = 0
t = 0
for line in data:
    parts = line.split()
    new_cur = (cur[0] + dirs[parts[0]][0] * int(parts[1]), cur[1] + dirs[parts[0]][1] * int(parts[1]))
    top = max(new_cur[0], cur[0])
    bot = min(new_cur[0], cur[0])
    min_y = min(bot, min_y)
    max_y = max(top, max_y)
    if parts[0] in ['R', 'L']:
        left = min(new_cur[1], cur[1])
        right = max(new_cur[1], cur[1])
        if new_cur[0] not in spots:
            spots[new_cur[0]] = []
        spots[new_cur[0]].append((left, right))
    else:
        for i in range(bot, top+1):
            if i not in spots:
                spots[i] = []
            spots[i].append((new_cur[1], new_cur[1]))
    cur = new_cur

ceiling = []
for i in range(min_y, max_y + 1):
    inside = False
    spots[i].sort()
    spots[i] = merge(spots[i])
    print(spots[i])
    for ind, interval in enumerate(spots[i]):
        t += (interval[1]-interval[0]+1)
        print((interval[1]-interval[0]+1))
        ceiling.append(interval)
        print('post', ceiling)
        ceiling.sort()
        ceiling = merge(ceiling)
        print('ceil', ceiling)
        if ind != len(spots[i])-1:
            amt = roofed((interval[1]+1, spots[i][ind+1][0]-1), ceiling)
            s += amt
            print('moo',amt)
        else:
            print(0)
print(t, s)
