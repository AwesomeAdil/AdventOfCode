import collections
from aocd import get_data
data = get_data(day=12, year=2022).split('\n')

move = list(zip([1, -1, 0, 0], [0, 0, 1, -1]))
q = collections.deque() # remember this for next time
stx = sty = ex = ey = 0
graph = [list(line) for line in data]
paths = []
spots = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 'S':
            graph[i][j] = ord('a')
            spots.append((i, j))
        elif graph[i][j] == 'E':
            graph[i][j] = ord('z')
            ex, ey = i, j
        else:
            if graph[i][j] == 'a':
                spots.append((i, j))
            graph[i][j] = ord(graph[i][j])

for sx, sy in spots:
    q.append((0, sx, sy))
    visited = set()
    while q:
        steps, x, y = q.popleft()
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if (graph[nx][ny] - 1) <= graph[x][y]:
                        if nx == ex and ny == ey:
                            paths.append(steps + 1)
                            if sx == stx and sy == sty:
                                print(steps+1)
                            q.clear()
                        q.append((steps + 1, nx, ny))

print(sorted(paths)[0])