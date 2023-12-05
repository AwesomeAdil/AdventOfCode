raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
ans = 0
mult = {}
mult[1] = 1
for index, line in enumerate(data):
    if index+1 not in mult:
        mult[index+1] = 1
    m = mult[index+1]
    del mult[index+1]
    words = line.split()
    winnings = words[2:12] # 12
    ours = words[13:] # 13
    num = len(set(ours).intersection(set(winnings)))
    ans += m
    for i in range(num):
        if index+i+2 not in mult:
            mult[index+i+2] = 1
        mult[index+i+2] += m
    print()
print(ans)

