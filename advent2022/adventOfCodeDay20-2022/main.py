from aocd import get_data
data = get_data(day=20, year=2022).split('\n')
values = []
values_to_move = {}

for index, line in enumerate(data):
    values.append(int(line) * 811589153)
    values_to_move[index] = (values[-1], index)

MOD = len(values)
for _ in range(10):
    for i in range(MOD):
        val, cur_loc = values_to_move[i]
        need_to_move = (val + cur_loc) % (MOD-1)
        values.pop(cur_loc)
        values.insert(need_to_move, val)
        values_to_move[i] = (val, need_to_move)
        for j in range(MOD):
            a, b = values_to_move[j]
            if cur_loc < b <= need_to_move and i != j:
                values_to_move[j] = (a, (b - 1) % MOD)
            elif cur_loc > b >= need_to_move and i != j:
                values_to_move[j] = (a, (b + 1) % MOD)

zero_loc = values.index(0)
groove = [values[(zero_loc + i) % MOD] for i in range(1000, 4000, 1000)]
print(sum(groove))