

def main():
    f = 2.3456789

    print('{:.2f}'.format(f))
    nums = [2, 5, 3, 2, 1, 0, 0, 8]
    n = len(nums)
    startID = 3
    ids = [startID]
    visited = [False] * n
    visited[startID] = True
    while ids:
        id = ids.pop()
        maxL, maxR = max(0, id - nums[id]), min(id + nums[id], n - 1)
        if id == n - 1 or maxR == n - 1:
            return True
        for i in range(maxL, id):
            if not visited[i]:
                visited[i] = True
                ids.append(i)
        for j in range(id+1, maxR):
            if not visited[j]:
                visited[j] = True
                ids.append(j)
    return False

if __name__ == '__main__':
    ret = main()
    print(ret)