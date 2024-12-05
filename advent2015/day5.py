raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

vowels = ['a', 'e', 'i','o','u']
def goodVowels(s):
    req = 3
    for c in s:
        if c in vowels:
            req -= 1
            if req == 0:
                return True
    return False
def goodDouble(s):
    for index, c, in enumerate(s[:-1]):
        if c == s[index+1]:
            return True
    return False



def goodPair(s):
    for i in range(len(s)-1):
        if s[i:i+2] in s[i+2:]:
            print(s[i:i+2])
            return True
    return False

def goodDouble_2(s):
    for index, c, in enumerate(s[:-2]):
        if c == s[index+2]:
            return True
    return False


def goodRes(s):
    for t in ["ab", "cd", "pq", "xy"]:
        if t in s:
            return False
    return True

ans = 0
part_2 = 0
for line in data:
    if goodVowels(line) and goodDouble(line) and goodRes(line):
        ans+=1
    if goodDouble_2(line) and goodPair(line):
        part_2+=1
print(ans,part_2)
