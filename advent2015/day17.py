raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
ans = 0
min_num = len(data)+5
num_ans = 0
for i in range(2**(len(data))+1):
    res = 0
    num = 0
    for j in range(len(data)):
        if (i>>j) & 1 == 1:
            num += 1
            res += int(data[j])
    if res == 150:
        if num < min_num:
            num_ans = 1
            min_num = num
        elif num == min_num:
            num_ans+=1
        ans+=1
print(ans, num_ans)
