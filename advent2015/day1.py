raw_data = open('sample.txt', 'r').read()
ans = 0
print(raw_data)
for index,i in enumerate(raw_data):
    if i == '(':
        ans+=1
    elif i == ')':
        ans-=1
    if ans <0:
        print(index+1)
        exit()
    
print(ans)
