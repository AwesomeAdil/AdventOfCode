from aocd import get_data
from aocd import submit

sample = open("sample.txt", "r").read()
answer = open("output.txt", "r").read()

act = int(answer) if answer.isnumeric() else -69


def solve(data, n):
    for i in range(len(data)):
        if len(set(data[i:i+n])) == n:
            return i+n


def answer():
    if sample == "" or act == -69:
        submit(solve(get_data(day=6, year=2022), 14), day=6, year=2022)
        return
    expected = solve(sample, 14)
    if expected == act:
        submit(solve(get_data(day=6, year=2022), 14), day=6, year=2022)
    else:
        print("Wrong answer!!")
        print("Your answer:", expected)
        print("Actual answer: ", act)


answer()
