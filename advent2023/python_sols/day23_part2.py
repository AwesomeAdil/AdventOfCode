from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

grid = {}
for r, line in enumerate(data):
    for c, ch in enumerate(line):
        grid[(r,c)] = ch

start = (0,1)
grid[(0,1)] = '#'
# compress
adjlist = {}
adjlist[start] = []
dirs = [(0,-1), (0,1), (1,0), (-1,0)]
"""
def compressed(spot, prev, dist):
    global adjlist, grid

    if spot == (len(data)-1, len(data)-2):
        if prev not in adjlist:
            adjlist[prev] = []
        adjlist[prev].append((spot, dist))
        return

    grid[spot] = '#'
    paths = []
    for dir in dirs:
        new_spot = tuple(map(sum, zip(dir, spot)))
        if new_spot in grid and grid[new_spot] != '#':
            paths.append(new_spot)

    if len(paths) > 1:
        if prev not in adjlist:
            adjlist[prev] = []
        adjlist[prev].append((spot, dist))
        print(adjlist[prev])
        for i in paths:
            compressed(i, spot,1)
    elif len(paths) == 1:
        compressed(paths[0], prev, dist + 1)

"""
print(len(data)-1, len(data)-2)
G = nx.Graph()
def comp2(spot):
    global adjlist, grid
    q = deque()
    q.append(((1,1), 1, spot))
    vis = set()
    while q:
        s, dist, prev = q.popleft()
        #if prev == (19, 19):
        #    print('woah')
        if s in vis:
            print('[nice]')
            break

        #if prev == (19, 19):
        #    print('woahhhhhh')
        while True:
            paths = []
            for dir in dirs:
                new_spot = tuple(map(sum, zip(dir, s)))
                if new_spot in grid and grid[new_spot] not in ['#','O'] and new_spot != prev:
                    paths.append(new_spot)
            

            if s in vis:
                """
                print(s, prev)
                for i in range(len(data)):
                    for j in range(len(data)):
                        print(grid[(i,j)], end='')
                    print()
                print()
                """
                if prev not in adjlist:
                    adjlist[prev] = []
                if s not in adjlist:
                    adjlist[s] = []

                G.add_edge(s, prev, weight = dist)
                adjlist[prev].append((s, dist))
                adjlist[s].append((prev, dist))
                break

            elif len(paths) == 1 and paths[0]==(len(data)-1, len(data)-2):
                if prev==(19,19):
                    print('a')
                G.add_edge(paths[0], prev, weight = dist+1)
                break
            if len(paths) == 0: 
                grid[s] = 'O'
                break
            elif len(paths) == 1 and paths[0]!=(len(data)-1, len(data)-2):
                grid[s] = 'O'
                s = paths[0]
                dist += 1
            else:
                """
                print(s, prev)
                for i in range(len(data)):
                    for j in range(len(data)):
                        print(grid[(i,j)], end='')
                    print()
                print()
                """
                vis.add(s)
                if prev not in adjlist:
                    adjlist[prev] = []
                if s not in adjlist:
                    adjlist[s] = []

                G.add_edge(s, prev, weight = dist)
                adjlist[prev].append((s, dist))
                adjlist[s].append((prev, dist))
                for p in paths:
                    q.append((p, 1, s))
                
                """
                if count > 2:
                    # Define layout (optional)
                    pos = nx.planar_layout(G)

                    # Draw nodes and edges
                    nx.draw(G, pos, with_labels=True)

                    # Draw edge labels
                    edge_labels = nx.get_edge_attributes(G, 'weight')
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

                    # Show the plot
                    plt.show()
                    exit()
                """
                break

def DFS(spot, vis = set()):
    res = 0
    vis.add(spot)
    for edge in G.edges(spot, data=True):
        target = edge[1]
        if target not in vis:
            weight = edge[2]['weight']
            res = max(res, weight + DFS(target, vis))
    vis.remove(spot)
    return res


comp2(start)
"""
for x,y in adjlist.items():
    print(x, y)
def findMax(spot, vis = set()):
    best = 0
    next_spot = (-1,-1)
    d = -1111
    if spot == (len(data), len(data[0])-1):
        return 0
    vis.add(spot)
    if spot in adjlist:
        for x,y in adjlist[spot]:
            if x in vis:
                continue
            res = y + findMax(x, vis)
            if res > best:
                best = res
                d = y
                next_spot = x
        print(spot, next_spot, d)
        vis.remove(spot)
        return best
    vis.remove(spot)
    return -100000

print(findMax(start))
"""

# Define layout (optional)
pos = nx.planar_layout(G)

# Draw nodes and edges
nx.draw(G, pos, with_labels=True)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#print(nx.shortest_path_length(G, source=(0,1), target = (22,21), weight='weight'))
# Show the plot
plt.show()
print(G.number_of_nodes(), G.number_of_edges())
print(DFS((0,1)))
#nx.draw_spring(G, with_labels=True)
#plt.show()
