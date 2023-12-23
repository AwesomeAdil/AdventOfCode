raw_data = open('sample.txt', 'r').read()
data = raw_data.split(',')

def hash(s):
    print(s)
    cv = 0
    for ch in s:
        cv += ord(ch)
        cv *= 17
        cv %= 256
    return cv

"""ans = 0
for i, x in enumerate(data):
    if i == len(data)-1:
        ans += hash(x[:-1])
    else:
        ans += hash(x)
print(ans)
"""
boxes = [[] for i in range(256)]
for i, x in enumerate(data):
    if i == len(data)-1:
        x = x[:-1]
    if '-' in x:
        label = x[:-1]
        boxes[hash(label)] = list(filter(lambda x: label not in x, boxes[hash(label)]))
    else:
        label, num = x.split('=')
        num = int(num)
        h = hash(label)
        found = False
        for x in boxes[h]:
            if x[0] == label:
                x[1] = num
                found = True
        if not found:
            boxes[h].append([label, num])

ans = 0
for i in range(256):
    for ind, x in enumerate(boxes[i]):
        ans += (i+1)*(ind+1)*x[1]
print(ans)
