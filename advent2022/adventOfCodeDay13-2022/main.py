from aocd import get_data
import functools

data = get_data(day=13, year=2022).split('\n\n')
result = 0


def compare(l, r):
    if l.isnumeric() and r.isnumeric():
        return int(l) - int(r)
    elif l.isnumeric():
        n = '[' + l + ']'
        return compare(n, r)
    elif r.isnumeric():
        n = '[' + r + ']'
        return compare(l, n)
    else:
        l1 = list(map(str, eval(l)))
        r1 = list(map(str, eval(r)))
        for x, y in zip(l1, r1):
            if compare(x, y):
                return compare(x, y)
        return len(l) - len(r)


sequences = []
for index, pair in enumerate(data, 1):
    left, right = pair.split('\n')
    sequences.extend(pair.split('\n'))
    result += index if compare(left, right) <= 0 else 0

sequences.extend(['[[2]]', '[[6]]'])
sorted_l = sorted(sequences, key=functools.cmp_to_key(compare))  #### REMEMBER THIS
print("Part 1:", result)
print("Part 2:", (sorted_l.index('[[2]]') + 1) * (sorted_l.index('[[6]]') + 1))
