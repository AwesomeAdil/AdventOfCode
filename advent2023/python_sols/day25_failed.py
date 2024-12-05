# DSU does not work as the interior structure of the graph also matters, we will 
# progress with Network flow now



raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]


parents = [{}, {}, {}, {}]
ranks = [{}, {}, {}, {}]
size = [{}, {}, {}, {}]
vals = set()

def findParent(x, l):
    global parents, ranks, size
    if x not in parents[0]:
        for p in range(4):
            parents[p][x] = x
            ranks[p][x] = 1
            size[p][x] = 1
    return x if parents[l][x] == x else findParent(parents[l][x], l)

def union(x,y):
    ind = 0
    while findParent(x, ind) == findParent(y,ind) and ind < 4:
        ind += 1

    if ind >= 4:
        print('fag')
        return

    x = findParent(x, ind)
    y = findParent(y, ind)

    if ranks[ind][x] < ranks[ind][y]:
        x, y = y, x

    size[ind][x] += size[ind][y]
    ranks[ind][x] = max(ranks[ind][x], ranks[ind][y] + 1)
    parents[ind][y] = x


for line in data:
    parts = line.split(': ')
    vals.add(parts[0])
    for i in parts[1].split():
        union(parts[0],i)
        vals.add(i)


for i in vals:
    if findParent(i, 2) == i:
        print(i,size[2][i])

