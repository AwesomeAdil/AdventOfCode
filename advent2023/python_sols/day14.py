raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
print(len(data), len(data[0]))

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
b = 1000000000
states = {}
grids = {}
state = 0
ans = {}
def move(grid):
    global state, states, ans
    hg = hashed(grid)
    print(cs(grid))
    if hg in states:
        print(states[grid], state)
        ind = (b - states[grid])%(state-states[grid]) + states[grid]
        print(ind, ans[ind])
        #print("ANS:", cs(grids[(1000000000-states[hg])%(state-states[hg]) + states[hg]]))
        return True, None

    rows = grid.split('\n')[:-1]
    spots = {}
    for x, row in enumerate(rows):
        for y, ch in enumerate(row):
            spots[(x,y)] = ch


    for index, dir in enumerate(dirs):
        if index % 2 == 0:
            for i in range(len(data[0])):
                if index == 0:
                    nextSpot = 0
                    for j in range(len(data)):
                        #print(j, i)
                        if spots[(j,i)] == '#':
                            nextSpot = j+1
                        elif spots[(j,i)] == 'O':
                            spots[(j, i)] = '.'
                            spots[(nextSpot, i)] = 'O'
                            nextSpot += 1
                else:
                    nextSpot = len(data)-1
                    for j in range(len(data[0])-1, -1, -1):
                        if spots[(j,i)] == '#':
                            nextSpot = j-1
                        elif spots[(j,i)] == 'O':
                            spots[(j, i)] = '.'
                            spots[(nextSpot, i)] = 'O'
                            nextSpot -= 1

        else:
            for i in range(len(data)):
                if index == 1:
                    nextSpot = 0
                    for j in range(len(data[i])):
                        if spots[(i,j)] == '#':
                            nextSpot = j+1
                        elif spots[(i,j)] == 'O':
                            spots[(i, j)] = '.'
                            spots[(i,nextSpot)] = 'O'
                            nextSpot += 1

                else:
                    nextSpot = len(data[0])-1
                    for j in range(len(data)-1, -1, -1):
                        if spots[(i, j)] == '#':
                            nextSpot = j-1
                        elif spots[(i, j)] == 'O':
                            spots[(i, j)] = '.'
                            spots[(i ,nextSpot)] = 'O'
                            nextSpot -= 1
        
    res = ""
    for row in range(len(data)):
        for col in range(len(data[0])):
            res += spots[(row, col)]
        res += '\n'
    states[grid] = state
    ans[state] = cs(grid)
    state+=1
    return False, res

def hashed(grid):
    ans = ""
    for row in grid:
        ans += str(row)
    return ans

def calcScore(data):
    grid = data.split('\n')[:-1]
    heights = {}
    amts = {}
    ans = 0
    blocked = set()
    for i, line in enumerate(grid):
        for c, ch in enumerate(line):
            if ch  == '#':
                blocked.add(c)
                heights[c] = len(grid)-i-1
                amts[c] = 0
            elif ch == 'O' and c not in blocked:
                if c not in amts:
                    amts[c] = 0
                ans += len(grid)-amts[c]
                amts[c]+=1
            elif ch == 'O':
                if c not in amts:
                    amts[c] = 0
                ans += heights[c] - amts[c]
                amts[c]+=1
    return ans 

def cs(grid):
    g = grid.split('\n')[:-1]
    ans = 0
    for i, line in enumerate(g):
        for c, ch in enumerate(line):
            if ch == 'O':
                ans += len(g) - i
    return ans

val, g = move(raw_data)
while not val:
    val, g = move(g)
