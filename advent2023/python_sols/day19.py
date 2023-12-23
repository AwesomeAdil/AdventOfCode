raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n\n')
x = 'x'
m = 'm'
a = 'a'
s = 's'

instructs = {}
instructs['A'] = 'A'
instructs['R'] = 'R'

def do2(ins, intervals = {x: (1, 4000), m: (1, 4000), a: (1, 4000), s:(1, 4000)}):
    for x in intervals.values():
        if x[0]>x[1]:
            return 0
    global instructs
    if ins == 'A':
        return getScore(intervals)
    if ins == 'R':
        return 0
    ans = 0
    inside = {x: y for x, y in intervals.items()}
    for a in ins[:-1]:
        #wow = str(d[a[0]]) + a[1] + a[2]
        outside = {x: y for x, y in inside.items()}
        if a[1] == '<':
            outside[a[0]] = (max(inside[a[0]][0], int(a[2])), max(inside[a[0]][1], int(a[2])-1))
            inside[a[0]] = (min(inside[a[0]][0], int(a[2])), min(inside[a[0]][1], int(a[2])-1))
        else:
            outside[a[0]] = (min(inside[a[0]][0], int(a[2])), min(inside[a[0]][1], int(a[2])))
            inside[a[0]] = (max(inside[a[0]][0], int(a[2]) +1), max(inside[a[0]][1], int(a[2])))
        
        ans += do2(instructs[a[3]], inside)
        inside, outside = outside, inside
    ans +=  do2(instructs[ins[-1]], inside)
    return ans



def getScore(interv):
    ans = 1
    for x in interv.values():
        ans *= (x[1]-x[0]+1)
    return ans

"""
def do(d, ins):
    global instructs
    if ins == 'A':
        return getScore(d)
    if ins == 'R':
        return 0

    for a in ins[:-1]:
        wow = str(d[a[0]]) + a[1] + a[2]
        if eval(wow):
            return do(d, instructs[a[3]])
    return do(d, instructs[ins[-1]])

def getScore(d):
    return sum(d.values())
"""



for line in data[0].split('\n'):
    label, rest = line.split("{")
    w = rest[:-1].split(',')
    temp = [x.split(':') for x in w]
    ins = [(a[0][0], a[0][1], a[0][2:], a[1]) for a in temp[:-1]]
    ins.append(temp[-1][0])
    instructs[label] = ins
"""    
ans = 0
for line in data[1].split('\n')[:-1]:
    moo = line.replace('=', ':')
    dic = eval(moo)
    ans += do(dic, instructs['in'])
"""
print(do2(instructs['in']))

