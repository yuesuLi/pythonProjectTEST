from collections import deque


def input_to_dependency_list(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    dependency_list = []
    for line in lines[1:]:
        dependency_list.append(list(map(int, line.split()))[1:])
    return N, dependency_list


def analyze_dependencies(N, dependency_list):
    indegree = [0] * (N + 1)
    for deps in dependency_list:
        for dep in deps:
            indegree[dep] += 1

    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    init_count = 0
    while queue:
        init_count += 1
        size = len(queue)
        for _ in range(size):
            module = queue.popleft()
            for dep in dependency_list[module - 1]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)

    if sum(indegree) != 0:
        return -1
    else:
        return init_count


def main():
    input_str1 = '''5
3 2 3 4
1 5
1 5
1 5
0'''

    input_str2 = '''3
1 2
1 3
1 1'''

    N1, dependency_list1 = input_to_dependency_list(input_str1)
    N2, dependency_list2 = input_to_dependency_list(input_str2)

    print(analyze_dependencies(N1, dependency_list1))  # 输出: 3
    print(analyze_dependencies(N2, dependency_list2))  # 输出: -1


if __name__ == '__main__':
    main()
from collections import deque


def input_to_dependency_list(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    dependency_list = []
    for line in lines[1:]:
        dependency_list.append(list(map(int, line.split()))[1:])
    return N, dependency_list


def analyze_dependencies(N, dependency_list):
    indegree = [0] * (N + 1)
    for deps in dependency_list:
        for dep in deps:
            indegree[dep] += 1

    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    init_count = 0
    while queue:
        init_count += 1
        size = len(queue)
