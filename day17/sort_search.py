import random
import time
import timeit  # 更精确的时间测量工具

# 快速排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# 二分查找
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 测试与优化
# 生成随机数据
start_data = time.time()
arr = random.sample(range(1, 1000000), 100000)  # 随机生成 100,000 个数据
end_data = time.time()
print(f"数据生成时间: {end_data - start_data:.6f} seconds")

# 快速排序
start_sort = time.time()
sorted_arr = quicksort(arr)
end_sort = time.time()
print(f"快速排序时间: {end_sort - start_sort:.6f} seconds")
print(f"sorted_arr 的前 10 个元素: {sorted_arr[:10]}")  # 检查排序结果

# 二分查找
# 使用 timeit 进行更精确的测量，运行多次取平均值
def run_binary_search():
    return binary_search(sorted_arr, 500000)

# 运行 1000 次二分查找，计算平均时间
binary_time = timeit.timeit(run_binary_search, number=1000) / 1000
result = binary_search(sorted_arr, 500000)
print(f"二分查找平均时间（1000 次运行）: {binary_time:.6f} seconds")
print(f"二分查找结果: {result}")
