from aocd import get_data
from aocd import submit

data = get_data(day=12, year=2021).split('\n')
#data = open("sample.txt", 'r').read().split('\n')

adjlist = {}
## REMEMBER .COPY()
def BFS():
    q = []
    q.append(("start", False, set()))
    result = 0
    while q:
        cave, twice, visited = q.pop(0)
        visited.add(cave)
        for item in adjlist[cave]:
            if item == 'start':
                continue
            elif item == 'end':
                result += 1
                continue
            elif item not in visited or item.isupper():
                q.append((item, twice, visited.copy()))
            elif not twice and item != 'start':
                q.append((item, True, visited.copy())) ## Remember that this took hours to figure out

    return result


def DFS(cur, visited, twice):
    if cur == 'end':
        return 1
    result = 0
    visited.add(cur)
    for i in adjlist[cur]:
        if i not in visited or i.isupper():
            result += DFS(i, visited.copy(), twice) ## Remember that this took hours to figure out
        elif not twice and i != 'start':
            result += DFS(i, visited.copy(), True)
    visited.discard(cur)
    return result




for x in data:
    a, b = x.split('-')
    if a not in adjlist:
        adjlist[a] = []
    if b not in adjlist:
        adjlist[b] = []

    adjlist[a].append(b)
    adjlist[b].append(a)

for item, val in adjlist.items():
    print(item, val)
print(DFS('start', set(), False))

