raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')
ans_1 = 0 
ans_2 = 0
for index, line in enumerate(data[:-1]):
    works = True
    moo=line.split()
    red = 0
    blue = 0
    green = 0
    for ind, word in enumerate(moo):
        if word.isnumeric():
            if moo[ind+1].startswith('red'): 
                works &= not int(word) > 12
                red = max(red, int(word))
            elif moo[ind+1].startswith('green'):
                works &= not int(word) > 13
                blue = max(blue, int(word))
            elif moo[ind+1].startswith('blue'):
                works &= not int(word) > 14 
                green = max(green, int(word))
    if works:
        ans_1 += index+1
    print(red, green, blue)
    ans_2 += red*green*blue
print(ans_1)
print(ans_2)
