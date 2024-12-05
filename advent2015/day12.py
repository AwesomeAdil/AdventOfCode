raw_data = open('sample.txt', 'r').read()
g = eval(raw_data)

def findNums(x):
    ans = 0
    if isinstance(x, int):
        return x
    if isinstance(x,str):
        return 0

    if isinstance(x,dict):
        for a,b in x.items():
            ans += findNums(a)
            ans += findNums(b)
            if b == 'red':
                return 0
    for a in x:
        ans += findNums(a)
    return ans

print(findNums(g))
