from aocd import get_data
data = get_data(day=22, year=2022).split('\n\n')
move = [(0,1), (1,0), (0, -1), (-1,0)]
pointer = ['>', 'v', '<', '^']
word_to_dir = {"right": 0, "left" : 2, "down": 1, "up": 3}
cur_face = 0
blocked = False
grid = list(line for line in data[0].split('\n'))
directions = data[1] + 'X'
cn = ""
cur_index = 0
cur_loc = ()
bounds_row = []
bounds_col = []

path = {}

def printBoard():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) == cur_loc:
                print(end = '*')
            elif (i, j) in path:
                print(end=pointer[path[(i, j)]])
            else:
                print(end='.' if grid[i][j] != ' ' else ' ')
        print()
    print('#'*30)
for row in grid:
    begin = len(row) + 5
    if '.' in row:
        begin = row.index('.')
    if '#' in row:
        begin = min(begin, row.index('#'))
    end = len(row) - 1
    bounds = (begin, end)
    bounds_col.append(bounds)

max_col = max(list(map(lambda x: len(x), grid)))
for index in range(max_col):
    found = False
    start = 0
    for i in range(len(grid)):
        end = len(grid) - 1
        if len(grid[i]) > index and not found and grid[i][index] != ' ':
            start = i
            found = True
        elif (len(grid[i]) <= index or grid[i][index] == ' ') and found:
            end = i - 1
            break
    bounds_row.append((start, end))



cur_loc = (0, 50) # remember to change
path[cur_loc] = cur_face
steps = 0
cols = 0
while cur_index < len(directions):
    cn += directions[cur_index]
    if not cn.isnumeric():
        colled = False
        amt = int(cn[:-1])
        dc = cn[-1]
        cn = ""
        oldx, oldy = cur_loc
        for i in range(amt):
            dx, dy = move[cur_face][0], move[cur_face][1]
            height = abs(bounds_row[cur_loc[1]][1] - bounds_row[cur_loc[1]][0])
            width = abs(bounds_col[cur_loc[0]][1] - bounds_col[cur_loc[0]][0])
            nx = oldx + dx
            ny = oldy + dy

            # Edge 5 -> 6 X
            to_face = cur_face
            blocked = False
            if nx == -1 and 50 <= ny <= 99 and cur_face == word_to_dir['up']:
                colled = True
                print('5 -> 6', oldx, oldy)
                nx = 100 + ny
                ny = 0
                print(nx, ny)
                to_face = word_to_dir["right"]
            # Edge 6 -> 5
            elif ny == -1 and 150 <= nx <= 199 and cur_face == word_to_dir['left']:
                colled = True
                print('6 -> 5', oldx, oldy)
                ny = nx - 100
                nx = 0
                print(nx, ny)
                to_face = word_to_dir['down']
            # Edge 3 -> 6 X
            elif nx == -1 and 100 <= ny <= 149 and cur_face == word_to_dir['up']:
                colled = True
                print('3 -> 6', oldx, oldy)
                nx = 199
                ny = ny - 100
                print(nx, ny)
                to_face = word_to_dir['up']
            # Edge 6 -> 3
            elif nx == 200 and 0 <= ny <= 49 and cur_face == word_to_dir['down']:
                colled = True
                print('6 -> 3', oldx, oldy)
                ny = ny + 100
                nx = 0
                print(nx, ny)
                to_face = word_to_dir['down']
            # Edge 5 -> 4 X
            elif 0 <= nx <= 49 and ny == 49 and cur_face == word_to_dir['left']:
                colled = True
                print('5 -> 4', oldx, oldy)
                nx = 149 - nx
                ny = 0
                print(nx, ny)
                to_face = word_to_dir['right']
            # Edge 4 -> 5
            elif 100 <= nx <= 149 and ny == -1 and cur_face == word_to_dir['left']:
                print('4 -> 5', oldx, oldy)
                nx = 149 - nx
                ny = 50
                print(nx, ny)
                to_face = word_to_dir['right']
            # Edge 3 -> 2 X
            elif 0 <= nx <= 49 and ny == 150 and cur_face == word_to_dir['right']:
                colled = True
                print('3 -> 2', oldx, oldy)
                nx = 149 - nx
                ny = 99
                print(nx, ny)
                to_face = word_to_dir['left']
            # Edge 2 -> 3
            elif 100 <= nx <= 149 and ny == 100 and cur_face == word_to_dir['right']:
                colled = True
                print('2 -> 3', oldx, oldy)
                nx = 149 - nx
                ny = 149
                print(nx, ny)
                to_face = word_to_dir['left']
            # Edge 1 -> 4
            elif 50 <= nx <= 99 and ny == 49 and cur_face == word_to_dir['left']:
                colled = True
                print('1 -> 4', oldx, oldy)
                ny = nx - 50
                nx = 100
                print(nx, ny)
                to_face = word_to_dir['down']
            # Edge 4 -> 1
            elif 0 <= ny <= 49 and nx == 99 and cur_face == word_to_dir['up']:
                colled = True
                print('4 -> 1', oldx, oldy)
                nx = 50 + ny
                ny = 50
                print(nx, ny)
                to_face = word_to_dir['right']
            # Edge 1 -> 3
            elif 50 <= nx <= 99 and ny == 100 and cur_face == word_to_dir['right']:
                colled = True
                print('1 -> 3', oldx, oldy)
                ny = 50 + nx
                nx = 49
                print(nx, ny)
                to_face = word_to_dir['up']
            # Edge 3 -> 1
            elif 100 <= ny <= 149 and nx == 50 and cur_face == word_to_dir['down']:
                colled = True
                print('3 -> 1', oldx, oldy)
                nx = ny - 50
                ny = 99
                print(nx, ny)
                to_face = word_to_dir['left']
            # Edge 2 -> 6
            elif nx == 150 and 50 <= ny <= 99 and cur_face == word_to_dir['down']:
                colled = True
                print('2 -> 6', oldx, oldy)
                nx = 100 + ny
                ny = 49
                print(nx, ny)
                to_face = word_to_dir['left']
            # Edge 6 -> 2
            elif 150 <= nx <= 199 and ny == 50 and cur_face == word_to_dir['right']:
                colled = True
                print('6 -> 2', oldx, oldy)
                ny = nx - 100
                nx = 149
                print(nx, ny)
                to_face = word_to_dir['up']


            # Part 1
            # if nx > bounds_row[cur_loc[1]][1]:
            #     nx = bounds_row[cur_loc[1]][0]
            # if ny > bounds_col[cur_loc[0]][1]:
            #     ny = bounds_col[cur_loc[0]][0]
            # if nx < bounds_row[cur_loc[1]][0]:
            #     nx = bounds_row[cur_loc[1]][1]
            # if ny < bounds_col[cur_loc[0]][0]:
            #     ny = bounds_col[cur_loc[0]][1]
            if grid[nx][ny] == '#':
                break
            else:
                cur_loc = (nx, ny)
                path[cur_loc] = cur_face
                oldx, oldy = (cur_loc)
                cur_face = to_face
        #print(amt, dc)
        cur_face += (1 if dc == 'R' else -1 if dc =='L' else 0)
        cur_face %= 4
    cur_index += 1


print("Part 1", 1000 * (cur_loc[0]+1) + 4 * (cur_loc[1]+1) + cur_face)