raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
backs = 0
ans = 0
ans_part2 = 0
for line in data:
    ans_part2 += line.count('\\') + line.count("\"")
    ans_part2 += 2

    ans += len(line)
    ans -= len(eval(line))
    backs += line.count('\\')
    backs += (line.count('\\x')*2)

print(ans_part2 , ans,len(data)*2+backs)

