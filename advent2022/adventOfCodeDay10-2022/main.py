from aocd import get_data


def print_spot():
    if rem % 40 == 0:
        print()
    proper_char = '*' if abs(ans - (rem % 40)) <= 1 else ' '
    print(end=proper_char)


data = get_data(day=10, year=2022).split('\n')
scores = [0 for _ in range(260)]
scores[0] = rem = ans = 1
print(end='\n*')

for i in data:
    a = i.split()
    scores[rem] = ans
    print_spot()
    if len(a) == 2:
        rem += 1
        scores[rem] = ans
        ans += int(a[1])
        print_spot()
    rem += 1

print(sum(list(map(lambda x: (40 * x[0] + 20) * x[1], enumerate(scores[20:260:40])))))
