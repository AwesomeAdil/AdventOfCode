raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
grid = {}

for r, line in enumerate(data):
    for c, ch in enumerate(line):
        grid[(r,c)] = ch

new_grid = {}

dirs = [(1,0), (1,-1), (1,1), (0,1), (0,-1), (-1,0),(-1,-1), (-1,1)]
#for x in range(len(data)):
#    for y in range(len(data)):
#        print(grid[(x,y)], end = '')
#    print()
#print()
for i in range(100):
    for x in range(len(data)):
        for y in range(len(data)):
            count = 0
            for dir in dirs:
                ns = tuple(map(sum, zip(dir, (x,y))))
                if ns in grid and grid[ns] == '#':
                    count += 1
            if x in [0, 99] and y in [0, 99]:
                new_grid[(x,y)] = '#'
            elif grid[(x,y)] == '#' and count in [2, 3]:
                new_grid[(x,y)] = '#'
            elif grid[(x,y)] == '.' and count == 3:
                new_grid[(x,y)] = '#'
            else:
                new_grid[(x,y)] = '.'
    for x in range(len(data)):
        for y in range(len(data)):
            grid[(x,y)] = new_grid[(x,y)]
            #print(grid[(x,y)], end = '')
        #print()
    #print()
    new_grid.clear()
        
ans = 0
for i in range(len(data)):
    for j in range(len(data)):
        if grid[(i,j)] == '#':
            ans += 1

print(ans)
