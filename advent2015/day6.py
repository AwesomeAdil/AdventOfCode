raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
lights = []
bright = []
num = 0
brightness = 0
for i in range(1000):
    lights.append([])
    bright.append([])
    for j in range(1000):
        lights[-1].append(False)
        bright[-1].append(0)



for line in data:
    words = line.split()
    a = ""
    b = ""
    if len(words) == 4:
        a, b  = words[1], words[3]
    else:
        a, b = words[2], words[4]
    ins = words[1]

    if words[0] == "toggle":
        ins = "toggle"
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))

    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            if ins == "toggle":
                if lights[i][j]:
                    num -= 1
                    lights[i][j]=False
                else:
                    num += 1
                    lights[i][j]=True
                brightness+=2
                bright[i][j] += 2
            elif ins == "off":
                if lights[i][j]:
                    num -= 1
                    lights[i][j] = False
                if bright[i][j] > 0:
                    brightness-=1
                    bright[i][j] -= 1
            elif ins == "on":
                if not lights[i][j]:
                    num += 1
                    lights[i][j] = True
                bright[i][j] += 1
                brightness += 1
print(num, brightness)
                
