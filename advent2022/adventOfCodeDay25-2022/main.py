raw = open('sample.txt', 'r').read().split('\n')
snap = {'1': 1, '2': 2, '-': -1, '=': -2, '0': 0}
deci = {key: val for val, key in snap.items()}
def to_decimal(snapu):
    res = 0
    for i, val in enumerate(snapu, 1):
        res += snap[val] * 5 ** (len(snapu) - i)
    return res

def to_snap(decimal):
    res = ""
    while decimal:
        remainder = decimal % 5
        if remainder > 2:
            decimal += 5
            remainder -= 5
        res = deci[remainder] + res
        decimal //= 5

    return res

ans = 0
for line in raw:
    print(line)
    ans += to_decimal(line)
    #print(to_decimal(line))

print(to_snap(ans))


