raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]

def calc_distance(speed,time_go, time_rest, time):
    distance = (speed*time_go) * (time//(time_go+time_rest))


    distance += speed * min(time%(time_go+time_rest), time_go)
    return distance

best_dist = 0
t = 1000 
scores = [0]*9
for i in range(1,t):
    best_spots = []
    best_dist = 0
    for index, line in enumerate(data):
        parts = line.split()
        s, tg, tr = int(parts[3]), int(parts[6]), int(parts[-2])
        res = calc_distance(s, tg, tr, i)
        if res > best_dist:
            best_spots = [index]
            best_dist =  res
        elif res == best_dist:
            best_spots.append(index)
    for ind in best_spots:
        scores[ind] += 1

print(max(scores))

