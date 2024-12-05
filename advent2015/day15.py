best = 0 
res = [(3, 0, 0, -3, 2), (-3,3,0,0,9), (-1, 0,4,0,1), (0,0,-2,2,8)]

def amt(x):
    global best, res
    mult = [0, 0, 0, 0, 0]
    for i in range(4):
        for j in range(5):
            mult[j] += x[i] * res[i][j]
    ans = 1
    for i in range(4):
        mult[i] = max(mult[i], 0)
        ans *= mult[i]
    if mult[4] == 500:
        best = max(best, ans)

for i in range(101):
    for j in range(i+1,101):
        for k in range(j+1, 101):
            i1 = i
            i2 = j-i
            i3 = k - j
            i4 = 100-k
            #exit()
            amt([i1,i2,i3,i4])
print(best)

