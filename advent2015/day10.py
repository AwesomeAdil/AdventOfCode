state = [(3,1), (1,3), (1,1), (2,2), (2,1), (1,3)]
#state = [(1,1)]

def merge():
    global state
    new_state = []
    index = 0
    while index < len(state):
        if index == len(state)-1:
            new_state.append(state[index])
            index+=1
        else:
            if state[index][1] == state[index+1][1]:
                #new_state.append((state[index][0]+state[index+1][0], state[index][1]))
                state[index+1] = (state[index][0]+state[index+1][0], state[index][1])
                index+=1
            else:
                new_state.append(state[index])
                index+=1
    state = new_state

def update():
    global state
    new_state = []
    for (x,y) in state:
        new_state.append((1,x))
        new_state.append((1,y))
    state = new_state
    merge()

def output():
    ans = ""
    for (x,y) in state:
        ans += str(y)*x
    return ans

def printSize():
    global state
    ans = 0
    for s in state:
        ans += s[0]
    print(ans)

for i in range(50):
    #print(output())
    update()
printSize()
