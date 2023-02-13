from aocd import get_data
from functools import reduce
data = get_data(day=16, year=2021)
#data = open("sample.txt", 'r').read()
to_bin = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}

result = ""
ans = 0
for x in data:
    result += to_bin[x]

def parse_packet(pac):
    vn = int(pac[0:3],2)
    pac = pac[3:]
    global ans
    ans += vn
    type = int(pac[0:3], 2)
    #print(f"Version Number: {vn} | Literal: {type == 4}")
    pac = pac[3:]
    num_trav = 6
    if type == 4:
        end = False
        val = ""
        while not end:
            end = (pac[0] == '0')
            val += pac[1:5]
            pac = pac[5:]
            num_trav += 5
        #print(f"Value is {int(val,2)}")
        return int(val,2), num_trav
    else:
        indicator = int(pac[0], 2)
        pac = pac[1:]
        num_trav += 1
        values = []
        if indicator == 0:
            num_bits = int(pac[:15], 2)
            #print(f"Num-bits: {num_bits}")
            pac = pac[15:]
            num_trav += 15
            amt = num_bits + num_trav
            while num_trav < amt:
                val, change = parse_packet(pac)
                num_trav += change
                pac = pac[change:]
                values.append(val)
        else:
            num_pacs = int(pac[:11], 2)
            #print(f"Num-pacs: {num_pacs}")
            pac = pac[11:]
            num_trav += 11
            for _ in range(num_pacs):
                val, change = parse_packet(pac)
                num_trav += change
                pac = pac[change:]
                values.append(val)

        response = -1
        if type == 0:
           response = sum(values)
        elif type == 1:
            response = reduce(lambda x, y: x * y, values)
        elif type == 2:
            response = min(values)
        elif type == 3:
            response = max(values)
        elif type == 5:
            response = 1 if (values[0] > values[-1]) else 0
        elif type == 6:
            response = 1 if (values[0] < values[-1]) else 0
        else:
            response = 1 if (values[0] == values[-1]) else 0

    return response, num_trav


print(parse_packet(result)[0])
print(ans)
