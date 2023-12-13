raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n\n')

ans = 0

def get_diff(a,b):
    ans = 0
    for x,y in zip(a,b):
        if x!=y:
            ans += 1
    return ans

def check_horz_sym(x, r):
    ans = 0
    for i in range(r+1):
        if 0<=r-i and r+i+1 < len(x):
            ans += get_diff(x[r-i], x[r+i+1])
            #if x[r-i] != x[r+i+1]:
            #    return False
    return ans == 1


def getCol(x, c):
    res = ""
    for i in range(len(x)):
        res+=x[i][c]
    return res

def check_vert_sym(x, c):
    ans = 0
    for i in range(c+1):
        if 0<=c-i and c+i+1 < len(x[0]):
            ans += get_diff(getCol(x, c-i), getCol(x, c+i+1))
            #if getCol(x, c-i) != getCol(x, c+i+1):
            #    return False
    return ans == 1

for index, group in enumerate(data):
    lines = group.split('\n')
    if index == len(data)-1:
        lines = lines[:-1]

    rows = len(lines)
    cols = len(lines[0])
    grid = {}
    found = False
    for row, line in enumerate(lines):
        if row < rows-1:
            if check_horz_sym(lines, row):
                ans += 100 * (row+1)
                print(row+1, line)
                found = True
                break
            else:
                for col, ch in enumerate(line):
                    grid[(row,col)] = ch
        else:
            for col, ch in enumerate(line):
                grid[(row,col)] = ch

    if found:
        continue
    for col in range(cols-1):
        if check_vert_sym(lines, col):
            ans += (col+1)
            break
print(ans)





