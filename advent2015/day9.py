from itertools import permutations
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
dists = {}
def calc_dists(x):
    sum_dist = 0
    for i in range(1, 8):
        sum_dist += dists[(x[i-1],x[i])]
    return sum_dist

index = 0
for i in range(7):
    for j in range(i+1,8):
        words = int(data[index].split()[-1])
        dists[(i,j)] = words
        dists[(j,i)] = words
        index += 1

ans_part1 = calc_dists([i for i in range(8)])
ans_part2 = ans_part1
for i in permutations(range(8)):
    ans_part1 = min(ans_part1, calc_dists(i))
    ans_part2 = max(ans_part2, calc_dists(i))
print(ans_part1, ans_part2)
