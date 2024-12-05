raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

temp = {"children" : "3", "cats":"7", "samoyeds": "2", "pomeranians": "3",
        "akitas": "0", "vizslas": "0","goldfish": "5","trees": "3","cars": "2",
        "perfumes": "1"}



for index, line in enumerate(data):
    parts = line.split(' ')[2:]
    works = True
    for i in range(len(parts)//2):
        if parts[2*i][:-1] in ["cats", "trees"]:
            works &= int(parts[2*i+1].split(',')[0]) > int(temp[parts[2*i][:-1]])
        elif parts[2*i][:-1] in ["pomeranians", "goldfish"]:
            works &= int(parts[2*i+1].split(',')[0]) < int(temp[parts[2*i][:-1]])
        else:
            print(parts[2*i][:-1])
            works &= int(parts[2*i+1].split(',')[0]) == int(temp[parts[2*i][:-1]])


        
    if works:
        print(index+1)
        exit()
        
