from aocd import get_data
from aocd import submit

sample = open("sample.txt", "r").read()
answer = open("output.txt", "r").read()
act = int(answer) if answer.isnumeric() else -69

points = {'X': 0, 'Y': 3, 'Z': 6}
points.update({"AX": 3, "AY": 1, "AZ": 2,
               "BX": 1, "BY": 2, "BZ": 3,
               "CX": 2, "CY": 3, "CZ": 1})


def solve(data):
    a = data.split('\n')
    score = 0
    for x in a:
        opp, me = x.split()
        comb = "" + opp + me
        score += points[me] + points[comb]
    return score


def answer():
    if sample == "" or act == -69:
        submit(solve(get_data(day=2, year=2022)), day=2, year=2022)
        return
    expected = solve(sample)
    if expected == act:
        submit(solve(get_data(day=2, year=2022)), day=2, year=2022)
    else:
        print("Wrong answer!!")
        print("Your answer:", expected)
        print("Actual answer: ", act)


answer()
