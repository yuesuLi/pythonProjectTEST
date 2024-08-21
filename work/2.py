class ResourcePool:
    def __init__(self, start_id, end_id):
        self.pool = list(range(start_id, end_id + 1))
        self.size = end_id - start_id + 1

    def allocate(self, id=None):
        if id is None:
            return self.pool.pop(0)
        else:
            if id in self.pool:
                self.pool.remove(id)
                return id
            else:
                return None

    def release(self, id):
        if id not in self.pool:
            self.pool.append(id)
            # self.pool.sort()

    def first_available(self):
        if len(self.pool) > 0:
            return self.pool[0]
        else:
            return None


# 读取输入
size_range = input().split()
pool_start = int(size_range[0])
pool_end = int(size_range[1])
pool = ResourcePool(pool_start, pool_end)

num_ops = int(input())
for i in range(num_ops):
    op = input().split()
    op_type = int(op[0])
    if op_type == 1:
        num_alloc = int(op[1])
        for j in range(num_alloc):
            pool.allocate()
            # print(pool.allocate(), end=' ')
    elif op_type == 2:
        id = int(op[1])
        pool.allocate(id)
        # print(pool.allocate(id))
    elif op_type == 3:
        id = int(op[1])
        pool.release(id)

# 输出结果
print(pool.first_available())
