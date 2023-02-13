import collections
from aocd import get_data
from aocd import submit

data = get_data(day=16, year=2022).split('\n')
adjlist = {}
worthit = {}
compressed = {}
dp = {}
count = 0


def DFS(cur, ele, time, etime, flowing):
    global dp
    if (time <= 1 and etime <= 1) or len(flowing) == count:
        return 0
    if (cur, ele, time, etime, flowing) in dp:
        return dp[(cur, ele, time, etime, flowing)]
    if (ele, cur, etime, time, flowing) in dp:
        return dp[(ele, cur, etime, time, flowing)]

    change_mine = change_ele = with_both = 0
    if (cur in flowing or compressed[cur][0] == 0) and time > 1:
        for adj, dist1 in compressed[cur][1]:
            if adj not in flowing and dist1 < time:
                change_mine = max(change_mine, DFS(adj, ele, time - dist1, etime, flowing))

    if (ele in flowing or compressed[ele][0] == 0) and etime > 1:
        for adj, dist1 in compressed[ele][1]:
            if adj not in flowing and dist1 < etime:
                change_ele = max(change_ele, DFS(cur, adj, time, etime - dist1, flowing))

    if cur not in flowing and compressed[cur][0] != 0 and compressed[ele][0] != 0 and ele not in flowing and cur != ele:
        with_both = max(time - 1, 0) * compressed[cur][0] + max(etime - 1, 0) * compressed[ele][0]
        new_flowing = [flow for flow in flowing]
        new_flowing.extend([cur, ele])
        new_flowing = tuple(sorted(new_flowing))
        change = 0
        change = max(change, DFS(cur, ele, time - 1, etime - 1, new_flowing))

        with_both += change

    dp[(cur, ele, time, etime, flowing)] = max(change_ele, change_mine, with_both)
    dp[(ele, cur, etime, time, flowing)] = dp[(cur, ele, time, etime, flowing)]
    return dp[(cur, ele, time, etime, flowing)]


for line in data:
    x = line.split()
    fr = int((x[4].split('=')[-1])[:-1])
    adjlist[x[1]] = (fr, set())
    if fr != 0:
        count += 1
    for tunnel in x[9:]:
        if tunnel != x[-1]:
            adjlist[x[1]][1].add(tunnel[:-1])
        else:
            adjlist[x[1]][1].add(tunnel)


def min_dist(start, end):
    q = collections.deque()
    q.append((start, 0))
    visited = set()
    while q:
        loc, dist = q.popleft()
        if loc in visited:
            continue
        if loc == end:
            return dist
        visited.add(loc)
        for adj in adjlist[loc][1]:
            if adj not in visited:
                q.append((adj, dist + 1))


important = {key for key, info in adjlist.items() if info[0] != 0 or key == 'AA'}
for key in important:
    fr, neighbors = adjlist[key]
    new_info = [(neighbor, min_dist(key, neighbor)) for neighbor in important if neighbor != key and (neighbor != 'AA')]
    compressed[key] = (fr, new_info)

submit(DFS('AA', 'AA', 26, 26, tuple()), day=16, year=2022)
