raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

ans = 0
for line in data:
    diff_list = []
    cur_list = list(map(int, line.split()))
    while not all([x == 0 for x in cur_list]):
        diff_list.append(cur_list)
        cur_list = [cur_list[i+1] - cur_list[i] for i in range(len(cur_list)-1)]
    
    i = len(diff_list)-1
    val = diff_list[i][0]
    while i>0:
        val = diff_list[i-1][0] - val 
        i-=1
    ans += val
print(ans)
