raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
letters = []
for i in range(26):
    letters.append(chr(ord("a")+i))

def first_req(x):
    rots = []
    for i in range(24):
        if (letters[i]+letters[i+1]+letters[i+2]) in x:
            return True
    return False

def second_req(x):
    return not ("i" in x or "l" in x or "o" in x)

def third_req(x):
    doubles = [letters[i]+letters[i] for i in range(26)]
    last = -5
    for i in range(len(x)-1):
        if x[i:i+2] in doubles and i!=last:
            if last != -5:
                return True
            else:
                last = i+1
    return False

def fix(x):
    for i in range(len(x)):
        if x[i] in ['i', 'l', 'o']:
            return x[:i] + chr(ord(x[i]) + 1) + 'a'*(len(x)-i-1)
    return x

def all(x):
    return first_req(x) and second_req(x) and third_req(x)

def update(x, c):
    if c == 0:
        return x
    if c == 1 and len(x) == 0:
        return "a"
    if c == 1 and x[-1] == 'z':
        return update(x[:-1], c) + "a"
    else:
        return x[:-1] + chr(ord(x[-1]) + 1) 

x = "hxbxxzaa"
while not all(x):
    #print(first_req(x), second_req(x), third_req(x))
    print(x)
    if not second_req(x):
        x = fix(x)
    else:
        x = update(x,1)
print(x)


