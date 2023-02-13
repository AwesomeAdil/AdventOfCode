from aocd import get_data
data = get_data(day=20, year=2021).split('\n')
#data = open('sample.txt', 'r').read().split('\n')
reference = data[0]


def addBorder(board, even):
    if even:
        newBoard = [list('.' * (len(board[0]) + 4)), list('.' * (len(board[0]) + 4))]
        for row in board:
            newBoard.append(list('..' + ''.join(row) + '..'))
        newBoard.append(list('.' * (len(board[0]) + 4)))
        newBoard.append(list('.' * (len(board[0]) + 4)))
        return newBoard
    else:
        newBoard = [list('#' * (len(board[0]) + 4)), list('#' * (len(board[0]) + 4))]
        for row in board:
            newBoard.append(list('##' + ''.join(row) + '##'))
        newBoard.append(list('#' * (len(board[0]) + 4)))
        newBoard.append(list('#' * (len(board[0]) + 4)))
        return newBoard


def transform(board, r, c):
    global reference
    res = ""
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            nr, nc = r + dr, c + dc
            try:
                res += "1" if board[nr][nc] == '#' else '0'
            except IndexError:
                print(nr,nc,len(board), len(board[3])-1)

    return reference[int(res, 2)]


grid = addBorder([line for line in data[2:]], True)
ox, oy = len(grid)-2, len(grid[0])-2
print(ox, oy)
for _ in range(2):
    grid = addBorder(grid, _%2==0)
    temp = [list(row) for row in grid]
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            temp[i][j] = transform(grid, i, j)
    grid = temp
for row in grid:
    print(''.join(row))
lights = 0
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[0])-1):
        if grid[x][y] == '#':
            lights+=1
print(lights)