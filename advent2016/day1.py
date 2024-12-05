import cmath
raw_data = open('sample.txt', 'r').read()
data = raw_data.split(', ')
spot = complex(0, 0)
dir = complex(0,1)
chg = {'R' : (1, -1), 'L': (-1, 1)}
locs = set()
locs.add((spot.real, spot.imag))
for i in data:
    dir = complex(dir.imag * chg[i[0]][0], dir.real * chg[i[0]][1])
    spot += dir * int(i[1:])
    if (spot.real, spot.imag) in locs:
        print('found')
        print(spot)
        break
    locs.add((spot.real, spot.imag))
print('DIst', abs(spot.real) + abs(spot.imag))
