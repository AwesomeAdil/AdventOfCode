from aocd import get_data

sample = open("sample.txt", "r").read()
data = get_data(day=7, year=2022).split('\n')
dict = {}
contains = {}


def DFS(cur):
    for item in contains[cur]:
        dict[cur] += DFS(item)
    return dict[cur]


for i in range(len(data)):
    x = data[i].split()
    if x[0] == '$':
        if x[1] == 'ls':
            continue
        cd = x[-1]
        if cd == "..":
            path.pop()
        elif cd == '/':
            path = []
        else:
            path.append(cd)
        s = '/' + '/'.join(path)
        if s not in dict:
            dict[s] = 0
            contains[s] = []

    elif x[0].isnumeric():
        dict[s] += int(x[0])
    else:
        if s == '/':
            contains[s].append('/' + x[-1])
        else:
            contains[s].append(s + '/' + x[-1])

DFS('/')
print(sum(list(map(lambda x: x if x <= 100000 else 0, dict.values()))))
unused = 70000000 - dict['/']
neededSpace = 30000000 - unused
minSeen = dict['/']
for key in dict.keys():
    if dict[key] >= neededSpace:
        minSeen = min(minSeen, dict[key])

print(minSeen)
