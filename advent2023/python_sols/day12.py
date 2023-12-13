import copy
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
ans = 0
memo = {}
def num_ways(a, b):
    h = hashed(b)
    if (a,h) in memo:
        return memo[(a,h)]

    if len(a) < sum(b):
        #print('x')
        return 0
    if sum(b) == 0 and '#' not in a:
        #print('y')
        return 1
    if sum(b) == 0 and '#' in a:
        #print('z')
        return 0
    d = copy.deepcopy(a)
    c = copy.deepcopy(b)

    if d[0] == '?':
        ans = 0
        ans += num_ways(d[1:], c)
        part = d[:c[0]]
        if '.' in part:
            memo[(a,h)] = ans
            return ans

        if len(d) > c[0] and d[c[0]] == '#':
            memo[(a,h)] = ans
            return ans

        if sum(c[1:]) > 0 and len(d) < c[0] + 1:
            memo[(a,h)] = ans
            return ans

        d = d[c[0]+1:]
        c = c[1:]
    
        if '#' not in d and sum(c)==0:
            memo[(a,h)] = ans + 1
            return ans + 1
        
        if '#' in d and sum(c) == 0:
            memo[(a,h)] = ans
            return ans

        ans += num_ways(d, c)
        memo[(a,h)] = ans
        return ans
    elif d[0] == '.':
        memo[(a,h)] = num_ways(d[1:], c)
        return memo[(a,h)]
    else:
        part = d[:c[0]]

        if '.' in part:
            return 0

        if len(d) > c[0] and d[c[0]] == '#':
            return 0

        if sum(c[1:]) > 0 and len(d) < c[0] + 1:
            return 0

        d = d[c[0]+1:]
        c = c[1:]

        if sum(c)== 0 and '#' not in d:
            return 1

        if sum(c) == 0 and '#' in d:
            return 0
        memo[(a,h)] = num_ways(d,c)
        return memo[(a,h)]
    return -1
def make_new(x):
    return x+'?'+x+'?'+x+'?'+x+'?'+x

def hashed(x):
    ans = 0
    for i in x:
        ans *= 15
        ans += i
    return ans

ans = 0
for index, line in enumerate(data):
    print(index)
    parts = line.split()
    comps = list(map(int, parts[-1].split(',')))
    add = num_ways(make_new(parts[0]), comps*5)
    ans += add

print(ans)
