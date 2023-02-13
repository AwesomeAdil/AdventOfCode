from aocd import get_data
from sympy import *
from math import ceil
data = get_data(day=21, year=2022).split('\n')

known = {}
unknown = {}
x = symbols('x')


def DFS(expression):
    global known
    global unknown
    if expression.isnumeric() or expression == 'x':
        return str(expression)
    thing = expression[1:-1]
    x, op, y = thing.split()
    if 'known[' in x:
        x = str(DFS(known[x[6:-1]]))
    if 'known[' in y:
        y = DFS(known[y[6:-1]])

    if x.isnumeric() and y.isnumeric():
        return str(eval(x + " " + op + " " + y))

    return str("(" + x + " " + op + " " + y + ")")


for line in data:
    x = line.split()
    if x[0] == 'humn:':
        known[x[0][:-1]] = "x"
    elif len(x) == 2:
            known[x[0][:-1]] = x[1]
    elif x[0] == 'root:':
        unknown[x[0][:-1]] = tuple([x[1], '==', x[-1]])
    else:
        unknown[x[0][:-1]] = tuple(x[1:])


while len(unknown):
    for key, val in unknown.items():
        first, op, second = val
        if first in known and second in known:
            operation = f"(known[{first}] {op} known[{second}])"
            known[key] = operation
            del unknown[key]
            break


first_half = known['root'].split()[0][1:]
second_half = known['root'].split()[-1][:-2]
print(simplify(DFS(known['dbcq'])), '=',  simplify(DFS(known['zmvq'])))
print(ceil((21608329599731.0 - 59466762521560)/- 11.3039388594944))