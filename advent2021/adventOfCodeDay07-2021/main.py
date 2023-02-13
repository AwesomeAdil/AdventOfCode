from aocd import get_data
from aocd import submit

sample = open("sample.txt", "r").read()
answer = open("output.txt", "r").read()

act = int(answer) if answer.isnumeric() else -69


def solve(data):
    file = data.split('\n')
    ans = 0
    for x in file:
        a = x.split()


    return ans


def answer():
    if sample == "" or act == -69:
        submit(solve(get_data(day=7, year=2022)), day=7, year=2022)
        return
    expected = solve(sample)
    if expected == act:
        submit(solve(get_data(day=7, year=2022)), day=7, year=2022)
    else:
        print("Wrong answer!!")
        print("Your answer:", expected)
        print("Actual answer: ", act)


answer()
