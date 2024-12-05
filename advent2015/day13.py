from itertools import permutations
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
adjlist = {}
def calc_happiness(x):
    min_con = 10000000000
    ans = 0
    for i in range(len(x)-1):
        ans += adjlist[(x[i], x[i+1])] + adjlist[(x[i+1], x[i])]
        min_con = min(min_con, adjlist[(x[i], x[i+1])] + adjlist[(x[i+1], x[i])])

    ans += adjlist[(x[-1], x[0])] + adjlist[(x[0], x[-1])]
    min_con = min(min_con, adjlist[(x[-1], x[0])] + adjlist[(x[0], x[-1])])

    return ans - min_con
index = 0
for i in range(8):
    for j in range(8):
        if i != j:
            words = data[index].split()[2:4]
            adjlist[(i, j)] = int(words[-1]) * (1 if words[0] == "gain" else -1)
            index += 1

ans = 0
for permuation in permutations(range(8)):
    ans = max(calc_happiness(permuation), ans)
print(ans)

