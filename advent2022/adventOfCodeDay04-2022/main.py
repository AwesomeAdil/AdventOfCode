from aocd import get_data
from aocd import submit

def solve(data):
    a = data.split('\n')
    ans = 0
    for x in a:
        l, r = x.split(',')
        l1, l2 = map(int, l.split('-'))
        r1, r2 = map(int, r.split('-'))
        if l2 >= r1 and r2 >= l1:
            ans += 1
    return ans

submit(solve(get_data(day=4, year=2022)), day=4, year=2022)