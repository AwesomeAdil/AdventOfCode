raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
ans_1 = 0
ans_2 = 0
for line in data:
    a, b, c = list(map(int, line.split('x')))
    ans_1 += 2 * (a*b + a*c + b*c) + min(a*b, min(a*c, b*c))
    ans_2 += 2*(a+b+c-max(a,max(b,c))) + a*b*c
print(ans_2)
    
