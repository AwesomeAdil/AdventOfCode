raw_data = open('sample.txt', 'r').read()

# 
spot_1 = (0,0)
spot_2 = (0,0)
s = set()
s.add(spot_1)
dirs = {'>': (1, 0), 'v': (0, -1), '<':(-1, 0), '^': (0, 1)}
for index, c in enumerate(raw_data):
    if c in dirs:
        if index % 2==0:
            spot_1 = (spot_1[0] + dirs[c][0], spot_1[1] + dirs[c][1])
            s.add(spot_1)
        else:
            spot_2 = (spot_2[0] + dirs[c][0], spot_2[1] + dirs[c][1])
            s.add(spot_2)

print(len(s))
