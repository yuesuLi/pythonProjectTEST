import heapq

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


n = int(input().strip())
k = int(input().strip())
monster_position = list(map(int, input().strip().split()))
people_position = list(map(int, input().strip().split()))

mymap = []
for i in range(n):
    mymap.append(input().strip().split())

flag = False


start = [people_position[2], people_position[3]]
end = [people_position[0], people_position[1]]
monsters = set()
for i in range(k):
    m = f'{monster_position[2*i]}_{monster_position[2*i+1]}'
    monsters.add(m)

all_postion = [(distance(start, end), start[0], start[1], 0)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
close_set = set()
while all_postion:
    f, i, j, g = heapq.heappop(all_postion)
    curr_state = f'{i}_{j}_{g}'
    if i == end[0] and j == end[1]:
        flag = True
        print(g)
        break

    if curr_state in close_set:
        continue
    close_set.add(curr_state)
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        xy = f'{new_i}_{new_j}'
        if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n and xy not in monsters and mymap[new_i][new_j][(g+1)%3] == '0':
            heapq.heappush(all_postion, (g+1+distance([new_i, new_j], end), new_i, new_j, g+1))




if not flag: print(0)