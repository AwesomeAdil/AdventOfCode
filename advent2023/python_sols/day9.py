raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def findDifferences(x):
    diffs = []
    for i in range(len(x)-1):
        diffs.append(x[i+1] - x[i])
    return diffs

def allZs(x):
    return len(x) == 0 or (len(set(x)) == 1 and x[0] == 0)

ans = 0
for line in data:
    diff_list = []
    cur_list = list(map(int, line.split()))
    while not allZs(cur_list):
        diff_list.append(cur_list)
        cur_list = findDifferences(cur_list)
    
    i = len(diff_list)-1
    val = diff_list[i][0]
    while i>0:
        val = diff_list[i-1][0] - val 
        i-=1
    ans += val
print(ans)
