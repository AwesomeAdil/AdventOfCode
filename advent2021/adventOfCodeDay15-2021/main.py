from queue import PriorityQueue
from aocd import get_data

pq = PriorityQueue()
data = get_data(day=15, year=2021).split('\n')
# data = open("sample.txt", 'r').read().split('\n')
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [list(map(int, list(line))) for line in data]
pq.put((0, 0, 0))
seen = {}


def dijkstras():
    while not pq.empty():
        risk, x, y = pq.get()
        if x == 5 * len(graph) - 1 and y == 5 * len(graph[-1]) - 1:
            return risk
        if (x, y) in seen:
            continue
        seen[(x, y)] = risk
        for cx, cy in zip(dx, dy):
            newX = x + cx
            newY = y + cy
            if 0 <= newX < 5 * len(graph) and 0 <= newY < 5 * len(graph[-1]) and (newX, newY) not in seen:
                # Prob can shorten this
                cost = graph[newX % (len(graph))][newY % (len(graph[-1]))]
                cost += newX // len(graph) + newY // len(graph[-1])
                cost -= 1
                cost %= 9
                cost += 1
                ### BRUH U FORGOT TO DO + RISK AT FIRST AND U IMPLEMENTED PRIMS AGAIN
                pq.put((cost + risk, newX, newY))


dp = {}


def memoization(r, c):
    if (r, c) in dp:
        return dp[(r, c)]

    if not (0 <= r < 5 * len(graph) and 0 <= c < 5 * len(graph[0])):
        return 1e9
    if r == 5 * len(graph) - 1 and c == 5 * len(graph[-1]) - 1:
        return (graph[r % len(graph)][c % len(graph[-1])] + r // len(graph) + c // len(graph[-1]) - 1) % 9 + 1

    miner = 1e9
    for cx, cy in zip(dx, dy):
        miner = min(miner, memoization(r + abs(cx), c + abs(cy)))
    dp[(r, c)] = (graph[r % len(graph)][c % len(graph[-1])] + r // len(graph) + c // len(graph[-1]) - 1) % 9 + 1 + miner
    return dp[(r, c)]


# sys.setrecursionlimit(2500)
# print(memoization(0,0) - graph[0][0])
print(dijkstras())
