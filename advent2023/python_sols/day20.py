from collections import deque
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

ffs = {}
cjs = {}
broad = []

low_c = 0
high_c = 0

memo = {}
col = []
index = 0
change_low = 0
change_high = 0
#imp 0 if low else 1
def doflip(x, imp):
    global ffs, change_low, change_high
    if imp == 1:
        return [], 0
    ret = []
    send = 1 if ffs[x][0] == 0 else 0
    ffs[x][0] = 1 - ffs[x][0]
    for i in ffs[x][1]:
        ret.append(i)
    #change_low += (1-send) * len(ffs[x][1])
    #change_high += send * len(ffs[x][1])
    return ret, send


def doconj(x, imp):
    global cjs, change_low, change_high
    res = 1 
    for i in cjs[x][0].values():
        res *= i
    send = 1 - res
    ret = []
    for i in cjs[x][1]:
        ret.append(i)
    #change_low += (1-send) * len(cjs[x][1])
    #change_high += send * len(cjs[x][1])
    return ret, send

def hash():
    global col
    s = ""
    for i in col:
        if i in ffs:
            s += str(ffs[i][0])
        elif i in cjs:
            for x in cjs[i][0].values():
                s += str(x)
    return s

def press():
    global index, change_low, change_high, memo, ffs, cjs, low_c, high_c
    index += 1
    q = deque()
    change_low = 1
    change_high = 0
    for i in broad:
        change_low += 1
        q.append((i,0, 'NAN'))
    

    #h = hash()
    #if h in memo:
    #    low_c += memo[h][0]
    #    high_c += memo[h][1]
    #    return 

    while q:
        item, x, par = q.popleft()
        #check vq, tf, db and ln
        if item == 'tg' and x == 1 and par == 'vq':
            print(index)
            exit()
        #print(item)
        if item in ffs:
            res,send = doflip(item, x)
            #print('low' if send == 0 else 'high')
            for i in res:
                q.append((i, send, item))
        elif item in cjs:
            cjs[item][0][par] = x
            res, send = doconj(item, x)
            #print('low' if send == 0 else 'high')
            for i in res:
                q.append((i, send, item))
    #memo[h] = (change_low, change_high)
    #low_c += change_low
    #high_c += change_high


for line in data:
    parts = line.split(' -> ')
    dests = parts[-1].split(', ')
    if parts[0][0] == '%':
        ffs[parts[0][1:]] = [0, dests] # off and dests
        col.append(parts[0][1:])
    elif parts[0][0] == '&':
        cjs[parts[0][1:]] = [{}, dests] # remembers low for start
        col.append(parts[0][1:])
    else:
        broad = dests



for i in col:
    if i in ffs:
        for j in ffs[i][1]:
            if j in cjs:
                cjs[j][0][i] = 0

index = 0
while True:
    #print(index)
    press()

print(low_c, high_c, low_c*high_c)
