from functools import cmp_to_key
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def compar(x, y):
    if ord(x) == ord(y):
        for a, b in zip(x, y):
            if cards.index(a)<cards.index(b):
                return 1
            elif cards.index(a)>cards.index(b):
                return -1
    if ord(x) > ord(y):
        return 1
    return -1

def ord(x):
    counts = {}
    num_joke = 0
    for i in x:
        if i == 'J':
            num_joke+=1
        else:
            if i not in counts:
                counts[i] = 0
            counts[i]+=1
    vals = []

    for e in counts.values():
        vals.append(e)
    vals.sort()

    if len(vals) == 0:
        return 5

    if num_joke == 0:
        if len(vals) == 1:
            return 5
        if len(vals) == 2:
            return vals[-1] # 4 if 4 kind 3 if full house
        if len(vals) == 3:
            if vals[-1] == 3:
                return 2 # three of a kind
            else:
                return 1 # two pair
        if len(vals) == 4:
            return 0 # one pair
        return -1 #high card
    else:
        if vals[-1] + num_joke == 5:
            return 5
        if vals[-1] + num_joke == 4:
            return 4
        if vals[-1] + vals[-2] + num_joke == 5:
            return 3
        if vals[-1] + num_joke == 3:
            return 2
        if vals[-1] + vals[-2] + num_joke == 4:
            return 1
        if num_joke == 1:
            return 0
    return -69

hands = {}
pos = []
for line in data:
    x, y = line.split()
    hands[x] = int(y)
    pos.append(x)

pos = sorted(pos, key=cmp_to_key(compar))
ans = 0
for index, el in enumerate(pos):
    ans+=(index+1)*hands[el]
print(ans)
