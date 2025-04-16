import numpy as np

arr = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])

print("原始数组：\n", arr)
print("数组加 5：\n", arr + 5)
print("数组平方：\n", arr ** 2)
print("第一行：", arr[0])
print("第二列：", arr[:, 1])
print("子数组：\n", arr[1:, 1:])# 从第一行/列开始到最后，不包括第一行/列

# 矩阵计算
matri1 = np.array([[1, 2], [3, 4]])
matri2 = np.array([[5, 6], [7, 8]])
print("矩阵相乘：\n", np.dot(matri1, matri2))

# 统计运算
print("最大值：", np.max(arr))
print("均值：", np.mean(arr))
print("按行求和：\n", np.sum(arr, axis=1))# axis=1 表示沿着列方向（横着加）,=0是按行计算

