from aocd import get_data
data = get_data(day=9, year=2022).split('\n')

visited = set()
motion = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
knots = [[0, 0] for i in range(10)]
visited.add((0, 0))
for line in data:
    a, b = line.split()
    for j in range(int(b)):
        knots[0] = [knots[0][0] + motion[a][0], knots[0][1] + motion[a][1]]
        for i in range(1, 10):
            dx = knots[i - 1][0] - knots[i][0]
            dy = knots[i - 1][1] - knots[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                knots[i][0] += 1 if dx > 0 else -1 if dx < 0 else 0
                knots[i][1] += 1 if dy > 0 else -1 if dy < 0 else 0
        visited.add((knots[9][0], knots[9][1]))

print(len(visited))
