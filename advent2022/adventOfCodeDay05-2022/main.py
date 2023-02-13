sample = open("sample.txt", "r").read()
answer = open("output.txt", "r").read()

act = int(answer) if answer.isnumeric() else -69


def solve(data):
    file = data.split('\n')
    start = found = 0
    stacker = [[] for i in range(9)]
    while not found:
        for i in range(9):
            if file[start][1] == '1':
                found = True
                break
            if ((4 * i + 1) >= len(file[start])) or (file[start][4 * i + 1] == ' '):
                continue
            stacker[i].append(file[start][4 * i + 1])
        start += 1

    for i in range(start+1, len(file)):
        x = file[i].split()
        a, b, c = map(int, list(x[1::2]))
        removed = stacker[b - 1][:a]
        # remove.reverse()
        stacker[b - 1] = stacker[b - 1][a:]
        removed.extend(stacker[c - 1])
        stacker[c - 1] = removed

    print(''.join([stacker[i][0] for i in range(len(stacker))]))
    return -1


solve(sample)
