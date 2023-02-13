from aocd import get_data
import math

data = get_data(day=21, year=2021).split('\n')

p1 = int(data[0][-1])
p2 = int(data[1][-1])

score_1 = 0
score_2 = 0
cur = 0
add_first = True

while score_1 < 1000 and score_2 < 1000:
    if add_first:
        p1 += 3 * cur + 5
        p1 %= 10
        p1 += 1
        score_1 += p1
    else:
        p2 += 3 * cur + 5
        p2 %= 10
        p2 += 1
        score_2 += p2
    cur += 3
    add_first = not add_first

print("Part 1:", min(score_1, score_2) * cur)

p1 = int(data[0][-1])
p2 = int(data[1][-1])
w1, w2 = 0, 0

dict = {}
amts = {3: 1, 9: 1, 4: 3, 8: 3, 5: 6, 7: 6, 6: 7}


def memoization(s1, s2, x1, x2):
    if (s1, s2, x1, x2) in dict:
        return dict[(s1, s2, x1, x2)]

    dict[(s1, s2, x1, x2)] = [0, 0]
    if s1 >= 21:
        return [1, 0]
    if s2 >= 21:
        return [0, 1]
    res = [0, 0]
    for i in range(2, 9):
        for j in range(2, 9):
            nx1 = (x1 + i) % 10 + 1
            nx2 = (x2 + j) % 10 + 1
            ns1 = nx1 + s1
            ns2 = nx2 + s2
            # If player 1 wins then no way player 2 rolls
            if(ns1 >= 21):
                res[0] += amts[i+1]
                break
            else:
                moo = list(map(lambda x: x * amts[i + 1] * amts[j + 1], memoization(ns1, ns2, nx1, nx2)))
                res[0] += moo[0]
                res[1] += moo[1]

    dict[(s1, s2, x1, x2)] = res


    return dict[(s1, s2, x1, x2)]


print("Part 2:",max(memoization(0, 0, p1, p2)))
