raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

values = {}
opp = {}
opps = ["AND", "OR", "RSHIFT", "LSHIFT", "NOT", "ASSIGN"]

actual_values = {}
def getVal(x):
    if x == 'b':
        return 956
    if x.isnumeric():
        return int(x)

    if x in actual_values:
        return actual_values[x]

    op = opp[x]
    if op == "ASSIGN":
        if values[x].isnumeric():
            actual_values[x] = int(values[x])
        else:
            actual_values[x] = getVal(values[x])
    elif op == "NOT":
        actual_values[x] = ~getVal(values[x])
    elif op == "AND":
        actual_values[x] = getVal(values[x][0]) & getVal(values[x][1])
    elif op == "OR":
        actual_values[x] = getVal(values[x][0]) | getVal(values[x][1])
    elif op == "RSHIFT":
        actual_values[x] = getVal(values[x][0]) >> getVal(values[x][1])
    elif op == "LSHIFT":
        actual_values[x] = getVal(values[x][0]) << getVal(values[x][1])

    return actual_values[x]

for line in data:
    parts = line.split(' -> ')
    comp = parts[0].split()
    if len(comp) == 1:
        opp[parts[-1]] = "ASSIGN"
        values[parts[-1]] = comp[0]
    elif len(comp) == 2:
        opp[parts[-1]] = "NOT"
        values[parts[-1]] = comp[1]
    else:
        opp[parts[-1]] = comp[1]
        values[parts[-1]] = [comp[0], comp[2]]

print(getVal('a'))

