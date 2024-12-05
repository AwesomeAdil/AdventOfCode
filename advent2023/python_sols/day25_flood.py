adjlist = {}
vis=set()
def sizer(spot):
    if spot in vis:
        return 0
    res = 1
    vis.add(spot)
    for i in adjlist[spot]:
        if i not in vis:
            res += sizer(i)
    return res


raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

for line in data:
    parts = line.split(': ')
    for x in parts[-1].split():
        if (parts[0], x) not in [('gbc', 'hxr'), ('hxr', 'gbc'), ('tmt', 'pnz'), ('pnz', 'tnt'), ('mvv', 'xkz'), ('xkz', 'mvv')]:
            if parts[0] not in adjlist:
                adjlist[parts[0]] = []
            if x not in adjlist:
                adjlist[x] = []

            adjlist[parts[0]].append(x)
            adjlist[x].append(parts[0])

a = sizer('tmt')
b = sizer('hxr')
print(a, b, a*b)
