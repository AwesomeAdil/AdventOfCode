import time
start_time = time.time()
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n\n')
seeds = list(map(int, data[0].split()[1:]))
ans = 10000000000000000
mapper = []
ranges = []
def findMapping(spot, i, c):
    if i == c:
            return spot

    for rang, dr in ranges[i].items():
        if rang[0]<=spot<=rang[1]:
            return findMapping(dr + (spot - rang[0]), i+1, c)


    return findMapping(spot, i+1, c)

def conv(x, y):
    return x[2] + y - x[0]

boundaries = []
for i in range(7):
    ranges.append({})
    boundaries.append([])
    moo = data[i+1].split('\n')[1:]
    for line in moo:
        if len(line.split()) != 3:
            break
        dr, sr, r = map(int,line.split())
        ranges[i][(sr, sr+r-1)] = dr
        boundaries[-1].append((sr, sr+r-1, dr))
    boundaries[-1].sort()

index = 0
seed_ranges = [(seeds[2*i], seeds[2*i]+seeds[2*i+1]-1) for i in range((len(seeds)+1)//2)]
seed_ranges.sort()
level = 0
for level in range(7):
    bi = 0
    new_ranges = []
    i = 0
    while i  < len(seed_ranges):
        seed_range = seed_ranges[i]
        while  bi < len(boundaries[level]) and boundaries[level][bi][1] < seed_range[0]:
            bi += 1

        if bi == len(boundaries[level]):
            new_ranges.append(seed_range)
            i+=1
            continue
        if boundaries[level][bi][0]<=seed_range[0] and seed_range[1] <= boundaries[level][bi][1]:
            a = conv(boundaries[level][bi], seed_range[0])
            b = conv(boundaries[level][bi], seed_range[1])
            new_ranges.append((a,b))
        elif seed_range[0] < boundaries[level][bi][0] <= seed_range[1]:
            temp = seed_range[1]
            a = seed_range[0]
            b = boundaries[level][bi][0]-1
            new_ranges.append((a,b))
            a = conv(boundaries[level][bi], boundaries[level][bi][0])
            if temp <= boundaries[level][bi][1]:
                b = conv(boundaries[level][bi], seed_range[1])
                new_ranges.append((a,b))
            else:
                new_ranges.append((conv(boundaries[level][bi], boundaries[level][bi][0]), conv(boundaries[level][bi], boundaries[level][bi][1])))
                seed_ranges.insert(i+1, (boundaries[level][bi][1]+1,temp))
        elif boundaries[level][bi][0] <= seed_range[0]:
            a = conv(boundaries[level][bi], seed_range[0])
            new_ranges.append((a, conv(boundaries[level][bi], boundaries[level][bi][1])))
            seed_ranges.insert(i+1, (boundaries[level][bi][1]+1,seed_range[1]))
        else:
            new_ranges.append(seed_range)
        i+=1

    new_ranges = list(set(new_ranges))
    new_ranges.sort()
    seed_ranges = new_ranges
print(seed_ranges[0][0])

end_time = time.time()
execution_time = abs(start_time - end_time)
print("Execution time:",execution_time)
