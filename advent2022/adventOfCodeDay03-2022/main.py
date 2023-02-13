from aocd import get_data
data = get_data(day=3, year=2022).split('\n')
res = 0
for i in range(0, len(data), 3):
    a, b, c = map(set, data[i:i+3])
    val = next(iter(a.intersection(b.intersection(c))))
    if ord('a') <= ord(val) <= ord('z'):
        res += ord(val) - ord('a') + 1
    else:
        res += ord(val) - ord('A') + 27
print(res)