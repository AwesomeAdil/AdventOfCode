raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def works(k, x, y):
    print(k*(x-k), y)
    return k*(x-k) > y

moo = data[0].split()[1:]
time = int(moo[0]+moo[1]+moo[2]+moo[3])

distance = data[1].split()[1:]


dist = int(distance[0] + distance[1] + distance[2] + distance[3])
print(time, dist)
left = 0
right = time // 2 
ans = right
while left <= right:
    print(left, right)
    mid = left+ (right-left)//2
    if(works(mid, time, dist)):
        right = mid-1
        ans = mid
    else:
        left = mid+1

print(ans)
print(time, dist)
print(time - (ans-1)*2)
