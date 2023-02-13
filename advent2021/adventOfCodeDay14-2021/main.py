from aocd import get_data
data = get_data(day=14, year=2021).split('\n')
#data = open("sample.txt", 'r').read().split('\n')
transform = {}
substrs = {}
phrase = data[0]

"""The slow way of solving for part I solution"""
# def step():
#     temp = ""
#     global phrase
#     for i in range(len(phrase)-1):
#         check = phrase[i:i+2]
#         if check in transform:
#             temp += check[0] + transform[check]
#         else:
#             temp += check[0]
#     phrase = temp + phrase[-1]

def step():
    updater = {}
    global substrs
    for x in substrs:
        if x in transform:
            left = x[0] + transform[x]
            right = transform[x] + x[1]
            if left in updater:
                updater[left] += substrs[x]
            else:
                updater[left] = substrs[x]
            if right in updater:
                updater[right] += substrs[x]
            else:
                updater[right] = substrs[x]
        else:
            if x in updater:
                updater[x] += substrs[x]
            else:
                updater[x] = substrs[x]
    substrs = updater


for i in range(len(phrase) - 1):
    if phrase[i:i + 2] in substrs:
        substrs[phrase[i:i + 2]] += 1
    else:
        substrs[phrase[i:i + 2]] = 1


for line in data[2:]:
    pair, insertion = line.split(' -> ')
    transform[pair] = insertion


for _ in range(40):
    step()

"""Part 1 calculation"""
# freqs = {}
# for let in phrase:
#     if let in freqs:
#         freqs[let] += 1
#     else:
#         freqs[let] = 1

freqs = {}
for sub in substrs:
    if sub[0] in freqs:
        freqs[sub[0]] += substrs[sub]
    else:
        freqs[sub[0]] = substrs[sub]
    if sub[1] in freqs:
        freqs[sub[1]] += substrs[sub]
    else:
        freqs[sub[1]] = substrs[sub]

freqs[phrase[0]] += 1
freqs[phrase[-1]] += 1
print(max(freqs.values())//2 - min(freqs.values())//2)