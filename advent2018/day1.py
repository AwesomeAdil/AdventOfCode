raw_data = open('sample.txt', 'r').read()
reached = set([0])
cur = 0
while True:
    for line in raw_data.split('\n')[:-1]:
        if line[0] == '+':
            cur += int(line[1:])
        else:
            cur -= int(line[1:])
        if cur not in reached:
            reached.add(cur)
        else:
            print('found')
            print(cur)
            exit()
print(cur)
