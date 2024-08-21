
# If you need to import additional packages or classes, please import here.


def distance(a, b):
    result = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return result

def func():

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

    import heapq
    n = int(input().strip())
    k = int(input().strip())
    monsterss = list(map(int, input().strip().split())) # k*2
    pose = list(map(int, input().strip().split()))  # 2*2
    mymap = []  # n*n
    for i in range(n):
        mymap.append(list(input().strip().split()))

    monsters = set()
    for m in range(k):
        monsters.add(f'{monsterss[m*2]}_{monsterss[m*2+1]}')

    start = [pose[2], pose[3]]
    end = [pose[0], pose[1]]
    visited = set()
    all_pos = [(distance(start, end), start[0], start[1], 0)]

    flag = False
    while all_pos:
        f, i, j, g = heapq.heappop(all_pos)
        if i == end[0] and j == end[1]:
            print(g)
            flag = True
            break

        if f'{i}_{j}_{g}' in visited:
            continue
        visited.add(f'{i}_{j}_{g}')

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
        for dir in dirs:
            pos = [i + dir[0], j + dir[1]]
            # if判断条件最后那里改成f'{pos[0]}_{pos[1]}' not in monsters好像也能通过
            if pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < n and mymap[pos[0]][pos[1]][(g+1)%3] == '0' and f'{i}_{j}' not in monsters:
                heapq.heappush(all_pos, (g+1+distance(pos, end), pos[0], pos[1], g+1))  # 这里distance前面加了个g+1其实是加的pos距离起点的距离（没考虑停下来的情况吗）
    if not flag: print(-1)



if __name__ == "__main__":
    func()
