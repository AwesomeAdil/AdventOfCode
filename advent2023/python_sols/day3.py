raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

ans_1 = 0
ans_2 = 0
grid = {}
spots = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1 ,1, -1, -1, 0, 1]
group = {}
gn = 0
for row, line in enumerate(data):
    numFar = ""
    for index, char in enumerate(line):
        if char.isdigit():
            numFar+=char
        else:
            for i in range(len(numFar)):
                grid[(row, index-i-1)] = numFar
                group[(row, index-i-1)] = gn
            gn += 1
            numFar = ""
            if char != '.':
                spots.append((row, index))
    if numFar != "":
        for i in range(len(numFar)):
            grid[(row, len(line)-i-1)] = numFar
            group[(row, len(line)-i-1)] = gn
        gn+=1
        numFar = ""
for spot in spots:
    adj = []
    for i in range(8):
        works = True
        nx = spot[0]+dx[i]
        ny = spot[1]+dy[i]
        if (nx, ny) in grid:
            for a in adj:
                if group[(nx, ny)] == group[a]:
                    print("nuhuh", grid[a])
                    works =  False
            if works:
                adj.append((nx, ny))

    ans_1 += sum(adj)       
    if len(adj) == 2:
        ans_2 += int(grid[adj[0]]) * int(grid[adj[1]])
        ## Part 1 code
          # ans += int(grid[(nx,ny)])
          #  #print(int(grid[(nx, ny)]))
          #  p = ny
          #  q = ny-1
          #  temp = grid[(nx, ny)]
          #  if dx[i] == 0:
          #      if dy[i] == 1:
          #          while (nx, p) in grid and grid[(nx, p)] == temp:
          #              del grid[(nx,p)]
          #              p += 1
          #      else:
          #          q = ny
          #          while (nx, q) in grid and grid[(nx, q)] == temp:
          #              del grid[(nx, q)]
          #              q-=1
          #  else:
          #      while (nx, p) in grid and grid[(nx, p)] == temp:
          #          del grid[(nx,p)]
          #          p += 1
          #      while (nx, q) in grid and grid[(nx, q)] == temp:
          #          del grid[(nx, q)]
          #          q-=1
print(ans)





