raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')

### Main issue for this day was that I only accounted for the first instance
# of a digit, now i know that rfind also gives me the last occurence.

## Can speed up by using methods isdigit, and startswith

ans_part1 = 0
ans_part2 = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    if(len(line) < 1):
        continue
    indicies_part1 = []
    indicies_part2 = []
    spot = {}

    # Added for the second part
    for index, num in enumerate(nums):
        if num in line:
            indicies_part2.append(line.find(num))
            indicies_part2.append(line.rfind(num))
            spot[line.find(num)] = index+1
            spot[line.rfind(num)] = index+1
    ###
    for i in range(10):
        if str(i) in line:
            indicies_part1.append(line.find(str(i)))
            indicies_part1.append(line.rfind(str(i)))
            indicies_part2.append(line.find(str(i)))
            indicies_part2.append(line.rfind(str(i)))
            spot[line.rfind(str(i))] = i
            spot[line.find(str(i))] = i

    ans_part1 += spot[min(indicies_part1)]*10 + spot[max(indicies_part1)]
    ans_part2 += spot[min(indicies_part2)]*10 + spot[max(indicies_part2)]
print(ans1, ans_part2)
