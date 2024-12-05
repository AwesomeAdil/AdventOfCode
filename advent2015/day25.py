import time
term = (2981, 3075)
point = (1,1)
cur = 20151125
prev = 2
while point != term:
    if prev != point[0] + point[1]:
        print(point[0] + point[1])
        prev = point[0] + point[1]
    cur = (cur * 252533)%33554393
    if point[0] == 1:
        point = (point[1]+1, 1)
    else:
        point = (point[0]-1,point[1]+1)
print(cur)
