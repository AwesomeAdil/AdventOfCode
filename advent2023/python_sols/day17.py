import heapq
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

scores = []
for line in data:
    scores.append([])
    for i in line:
        scores[-1].append(int(i))


points = []
heapq.heappush(points, (0, (-1, -1), 0, (0,0)))


dir = [(1, 0), (0,1), (-1,0), (0,-1)]
visited = set()

dist = {}
dirs = {}
while points:
    p = heapq.heappop(points)
    if p[-1] in dist and (p[1],p[2]) in dirs[p[-1]] and dist[p[-1]] <= p[0]:
        continue

    dist[p[-1]] = p[0]
    if p[-1] not in dirs:
        dirs[p[-1]] = set()
    dirs[p[-1]].add((p[1], p[2]))

    if p[-1] == (len(data)-1, len(data[0])-1) and p[2] >= 4:
        print(p[0])
        exit()
    for d in dir:
        nx, ny = p[-1][0] + d[0], p[-1][1] + d[1]
        if (p[1] == d and p[2] == 10):
            continue
        if(p[1]!=d and p[2] < 4 and p[-1] != (0,0)):
            continue
        if d[0] == -1 * p[1][0] and d[1] == -1*p[1][1]:
            continue
        if 0<=nx<len(data) and 0<=ny<len(data[0]):
            if d == p[1]:
                heapq.heappush(points, (scores[nx][ny] + p[0], d,p[2] + 1, (nx, ny)))
            else:
                heapq.heappush(points, (scores[nx][ny] + p[0], d,1, (nx, ny)))
