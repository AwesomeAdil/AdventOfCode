# the most important function, need to remember
def factor(x):
    factors = []
    i = 2
    while i <= (x**(1/2)):
        cnt = 0
        while x % i == 0 and x > 0:
            x /= i
            cnt += 1
        if cnt > 0:
            factors.append((i, cnt))
        i += 1
    if x > 1:
        factors.append((x, 1))
    return factors

def sum_of_div(x):
    ans = 1
    facts = factor(x)
    for f in facts:
        ans *= (f[0]**(f[1]+1)-1)//(f[0]-1)
    return ans * 10

best = 11
bl = 1
i = 1
sd = {}
while best < 36000000:
    print(best)
    for j in range(50):
        if i * (j+1) not in sd:
            sd[i*(j+1)] = 0
        sd[i*(j+1)] += i * 11
        if best < sd[i]:
            best = sd[i]
            bl = i
            if best >= 36000000:
                break
    i += 1
print(bl)



