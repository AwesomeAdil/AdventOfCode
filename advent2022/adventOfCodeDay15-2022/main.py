from aocd import get_data

data = get_data(day=15, year=2022).split('\n')

ranges = {}
boundary = 4000000


def get_num_ranges(arr):
    old_l, old_r = arr[0]
    amt = old_r - old_l + 1
    for nl, nr in arr[1:]:
        if nr <= old_r:
            continue
        elif nl <= old_r:
            amt += nr - old_r
            old_r = nr
        else:
            amt += nr - nl + 1
            old_l, old_r = nl, nr
    return amt - 1


def skips(arr, bound):
    old_l, old_r = arr[0]
    amt = old_r - old_l + 1
    for nl, nr in arr[1:]:
        if nl > bound:
            return -1
        if nr < old_r:
            continue
        elif nl <= old_r:
            amt += nr - old_r
            old_r = nr
        else:
            if bound > nl > old_r + 1:
                return nl - 1
            amt += nr - nl + 1
            old_l, old_r = nl, nr
    return -1


for line in data:
    print(line)
    sensor_x, sensor_y = map(lambda x: int(x[2: -1]), line.split()[2: 4])
    beacon_x = int((line.split()[-2])[2:-1])
    beacon_y = int((line.split()[-1])[2:])
    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    for height in range(-dist + 1, dist):
        h = height + sensor_y
        if h not in ranges:
            ranges[h] = []
        ranges[h].append((sensor_x - dist + abs(height), sensor_x + dist - abs(height)))
        ranges[h].sort()

# Part 1
level = 2000000
print("Part 1:", get_num_ranges(ranges[level]))

# Part 2
for range in range(boundary):
    if skips(ranges[range], boundary) > 0:
        print("Part 2:", range + skips(ranges[range], boundary) * 4000000)