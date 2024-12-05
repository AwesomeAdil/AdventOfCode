best = 0 
res = [(-1,-2,6,3,8),(2,3,-2,-1,3)]
a, b = -1, -1
def amt(x):
    global best, res, a, b
    mult = [0, 0, 0, 0, 0]
    for i in range(2):
        for j in range(5):
            mult[j] += x[i] * res[i][j]
    ans = 1
    for i in range(4):
        if mult[i] > 0:
            ans *= mult[i]
        else:
            ans = 0

    if best < ans:
        a,b= x[0], x[1]
    
    if mult[4] == 500:
        best = max(best, ans)

for i in range(101):
    i1 = i
    i2 = 100 - i
    amt([i1,i2])
print(best)
print(a, b)
