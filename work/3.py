def batch_init(dependencies):
    # 初始化每个模块的入度
    in_degree = [0] * len(dependencies)
    for i in range(len(dependencies)):
        for j in range(1, len(dependencies[i])):
            in_degree[dependencies[i][j] - 1] += 1

    # 将入度为0的模块加入队列
    queue = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    # 计算批量初始化的次数
    count = 0
    while queue:
        # 每次从队列中取出一个入度为0的模块
        module = queue.pop(0)
        count += 1
        # 将该模块所依赖的模块的入度减1
        for i in range(1, len(dependencies[module])):
            in_degree[dependencies[module][i] - 1] -= 1
            # 如果减1后入度为0，则加入队列
            if in_degree[dependencies[module][i] - 1] == 0:
                queue.append(dependencies[module][i] - 1)

    # 如果存在入度不为0的模块，则说明存在循环依赖，返回-1
    if sum(in_degree) > 0:
        return -1
    else:
        return count


if __name__ == '__main__':
    n = int(input())
    dependencies = []
    for i in range(n):
        line = input().split()
        if int(line[0]) == 0:
            dependencies.append([])
        else:
            dependencies.append([int(x) for x in line[1:]])

    result = batch_init(dependencies)
    print(result)