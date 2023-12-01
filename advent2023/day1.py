raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')

### Main issue for this day was that I only accounted for the first instance
# of a digit, now i know that rfind also gives me the last occurence.

## Can speed up by using methods isdigit, and startswith -> johnathanpaulson

#ans = 0
#for line in data:
#    found = 10
#    last = -1
#    for char in line:
#        if not (ord('a')<=ord(char)<=ord('z')):
#            if found == 10:
#                ans += found*int(char)
#            print(found * int(char), ans)
#            found = 1
#            last = int(char)
#    ans += last
#print(ans+1)
ans = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    if(len(line) < 1):
        continue
    indicies = []
    spot = {}

    for index, num in enumerate(nums):
        if num in line:
            indicies.append(line.find(num))
            indicies.append(line.rfind(num))
            spot[line.find(num)] = index+1
            spot[line.rfind(num)] = index+1

    for i in range(10):
        if str(i) in line:
            indicies.append(line.find(str(i)))
            indicies.append(line.rfind(str(i)))
            spot[line.rfind(str(i))] = i
            spot[line.find(str(i))] = i

    ans += spot[min(indicies)]*10 + spot[max(indicies)]
print(ans)

