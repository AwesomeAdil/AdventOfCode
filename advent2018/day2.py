raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
two = 0
three = 0

def diff(x, y):
    res = 0
    for a, b in zip(x, y):
        if a!=b:
            res += 1
        if res >= 2:
            return False
    return True

def iff(x, y):
    res = ""
    for a, b in zip(x, y):
        if a==b:
            res += a
    return res


col = []

for line in data:
    for x in col:
        if diff(x, line):
            print(iff(x, line))
            exit()
    col.append(line)
    counts = {}
    for ch in line:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    if 2 in counts.values():
        two += 1
    if 3 in counts.values():
        three += 1
print(two * three)

