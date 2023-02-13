sx, ex, sy, ey = 150, 193, -136, -86
print("Part 1:", (abs(sy) * (abs(sy) - 1)) // 2)
ans = 0


def work(vx, vy):
    cx, cy = 0, 0
    while cx <= ex:
        if sx <= cx <= ex and sy <= cy <= ey:
            return True
        if (vy < 0 and cy < sy) or (vx == 0 and cx < sx):
            return False
        cx += vx
        cy += vy
        vx = max(0, vx - 1)
        vy = vy - 1
    return False


for i in range(350):
    for j in range(-500, 500):
        if work(i, j):
            ans += 1

print("Part 2:", ans)
