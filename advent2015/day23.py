raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

ins = 0
vals = {}
vals['a'] = 1
while 0<=ins<len(data):
    parts = data[ins].split()
    if parts[0] == 'hlf':
        reg = parts[1]
        if reg not in vals:
            vals[reg] = 0
        vals[reg] /= 2
        ins += 1
    elif parts[0] == 'tpl':
        reg = parts[1]
        if reg not in vals:
            vals[reg] = 0
        vals[reg] *= 3
        ins += 1
    elif parts[0] == 'inc':
        reg = parts[1]
        if reg not in vals:
            vals[reg] = 0
        vals[reg] += 1
        ins += 1
    elif parts[0] == 'jmp':
        if parts[1][0] == '+':
            ins += int(parts[1][1:])
        else:
            ins -= int(parts[1][1:])
    elif parts[0] == 'jie':
        reg = parts[1][:-1]
        if reg not in vals:
            vals[reg] = 0
        if vals[reg] % 2 == 0:
            if parts[-1][0] == '+':
                ins += int(parts[-1][1:])
            else:
                ins -= int(parts[-1][1:])
        else:
            ins += 1
    else:
        reg = parts[1][:-1]
        if reg not in vals:
            vals[reg] = 0
        if vals[reg] == 1:
            if parts[-1][0] == '+':
                ins += int(parts[-1][1:])
            else:
                ins -= int(parts[-1][1:])
        else:
            ins += 1
    print(vals)

print(vals['b'])
