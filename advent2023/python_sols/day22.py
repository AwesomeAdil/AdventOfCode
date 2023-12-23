from collections import deque
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]


def intersect(l1, l2):
    # Vert
    if l1 == [[-1000, 1000], [-1000, 1000]] or l2 == [[-1000, 1000], [-1000, 1000]]:
        return True

    #print(l1, l2)
    if l1[0][0] == l1[1][0]:
        if l2[0][0] == l2[1][0]:
            #print('A')
            a, b, x, y = min(l1[0][1], l1[1][1]), max(l1[0][1], l1[1][1]), min(l2[0][1], l2[1][1]), max(l2[0][1], l2[1][1])
            #print(a, b, x, y)
            return l1[0][0] == l2[0][0] and (a<=x<=b or x<=a<=y)
        else:
            l = min(l2[0][0], l2[1][0])
            r = max(l2[0][0], l2[1][0])
            x = min(l1[0][1], l1[1][1])
            y = max(l1[0][1], l1[1][1])
            #print(l, l1[0][0], r, x,l2[0][1], y)
            
            #print('B')
            return l <= l1[0][0] <= r and x <= l2[0][1] <= y
    else:
        if l2[0][1] == l2[1][1]:
            #print('C')
            a, b, x, y = min(l1[0][0], l1[1][0]), max(l1[0][0], l1[1][0]), min(l2[0][0], l2[1][0]), max(l2[0][0], l2[1][0])
            return l1[0][1] == l2[0][1] and (a<=x<=b or x<=a<=y)
        else:
            l = min(l2[0][1], l2[1][1])
            r = max(l2[0][1], l2[1][1])
            x = min(l1[0][0], l1[1][0])
            y = max(l1[0][0], l1[1][0])
            #print('D')
            #print(l, r, x, y)
            return l <= l1[0][1] <= r and x <= l2[0][0] <= y

def anser(x, dep, sup):
    res = set()
    works = False
    covered = set([x])
    all = deque()
    all.append(x)
    while all:
        top = all.popleft()
        for j in sup[top]:
            if j in covered:
                continue
            if len(dep[j] & covered) == len(dep[j]):
                all.append(j)
                covered.add(j)
    return len(covered)-1

def con(x, sup, covered):
    ans = set([x])
    for i in sup[x]:
        ans.update(con(i, sup))
    return ans



bricks = []
for line in data:
    end_points = line.split('~')
    start = list(map(int,end_points[0].split(',')))
    end = list(map(int, end_points[1].split(',')))
    if start[-1] > end[-1]:
        start, end = end, start
    bricks.append((start, end))
bricks = sorted(bricks, key=lambda x: x[0][-1])
lowest_level = 1
layers = [[[-1000, 1000], [-1000,1000]]]
height = [0]
depends = {}
depends[0]=set()
supports = {}
supports[0]=set()
for i in range(len(bricks)):
    new_layer = [bricks[i][0][:2], bricks[i][1][:2]]
    supports[i+1] = set()
    depends[i+1] = set()
    height.append(-1000)
    for j in range(len(layers)):
            lay = layers[j]
            if intersect(new_layer, lay):
                #print('A')
                #print(i+1, j, new_layer, lay)
                if height[-1] < height[j] + (bricks[i][1][-1] - bricks[i][0][-1]) + 1:
                    for x in depends[i+1]:
                       # print('SUPPORT', i+1, supports[j])
                        supports[x].remove(i+1)
                       # print('SUPPORT', i+1, supports[j])
                    height[-1] = height[j] + (bricks[i][1][-1] - bricks[i][0][-1]) + 1
                    supports[j].add(i+1)
                    depends[i+1] = set([j])
                elif height[-1] == height[j] + (bricks[i][1][-1] - bricks[i][0][-1]) + 1:
                    #print('B')
                    supports[j].add(i+1)
                    depends[i+1].add(j)

    layers.append(new_layer)
if -1000 in height:
    print('uh oh')
    exit()
pans = 0
"""
for i in range(len(bricks)):
    works = True
    for j in supports[i+1]:
        if len(depends[j]) == 1:
            works = False
    if works:
          ans += 1
print(ans, pans)
"""
for x in range(len(bricks)):
    pans += anser(x+1, depends, supports)
print(pans)
#print(height)
#print(supports)
#print(depends)
#print(intersect([[0, 0], [0, 5]], [[0,6], [0,9]]))
