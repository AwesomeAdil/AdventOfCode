import numpy as np
import sympy
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

locs = []
vels = []

#left_b = 7
#right_b = 27
left_b = 200000000000000
right_b = 400000000000000

def intersection_2D(x, y):
    loc1, vel1 = locs[x], vels[x]
    loc2, vel2 = locs[y], vels[y]
    A = np.array([[-1 * vel1[1], vel1[0]], [-1 * vel2[1], vel2[0]]])
    b = np.array([[vel1[0]*loc1[1]-vel1[1]*loc1[0]], [vel2[0] * loc2[1] - vel2[1]*loc2[0]]])
    det = np.linalg.det(A)
    if det == 0:
        return False
    A_ = np.linalg.inv(A) 
    res = np.matmul(A_, b)
    div = vel1[1]
    time1 = -1
    if vel1[0] != 0:
        div = vel1[0]
        time1 = (res[0, 0] - loc1[0])/div
    else: 
        time1 = (res[1, 0] - loc1[1])/div

    div = vel2[1]
    time2 = -1
    if vel2[0] != 0:
        div = vel2[0]
        time2 = (res[0, 0] - loc2[0])/div
    else: 
        time2 = (res[1, 0] - loc2[1])/div

    return time1 >= 0 and time2 >= 0 and left_b <= res[0, 0] <= right_b and left_b <= res[1, 0] <= right_b

def symp():
    # knowing that t = (x_h - x_r)/(vx_h - vx_r) = (y_h - y_r)/(vy_h - vy_r) = (z_h - z_r)/(vz_h - vz_r)
    # we dont need that many cases
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
    equations = []
    for loc, vel in list(zip(locs, vels))[:4]:
        sx, sy, sz = loc
        vx, vy, vz = vel
        #print(sx, sy, sz, vx, vy, vz)
        equations.append((xr - sx) * (vyr - vy) - (yr - sy) * (vxr - vx))
        equations.append((zr - sz) * (vyr - vy) - (yr - sy) * (vzr - vz))

    answers = sympy.solve(equations)[0]
    print(answers[xr] + answers[yr] + answers[zr])


for line in data:
    loc, vel = line.split(' @ ')
    loc = list(map(int, loc.split(', ')))
    vel = list(map(int, vel.split(', ')))
    locs.append(loc)
    vels.append(vel)

ans = 0

for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if intersection_2D(i,j):
            ans += 1

print(ans)
symp()
