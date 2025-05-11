import time

# 列表查找优化
numbers = [i for i in range(1000000)]
start = time.time()
check = 999999 in numbers  # 列表查找
end = time.time()
print(f"List search time: {end - start}")

# 集合查找优化
numbers_set = set(numbers)
start = time.time()
check = 999999 in numbers_set  # 集合查找
end = time.time()
print(f"Set search time: {end - start}")
