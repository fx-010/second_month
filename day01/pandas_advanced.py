import pandas as pd

customers = pd.read_csv(r"E:\second_month\day01\customers.csv")
orders = pd.read_csv(r"E:\second_month\day01\orders.csv")

# 分组聚合：计算每个类别的总销售额
category_sales = orders.groupby("Category")["Amount"].sum().reset_index()
# print(category_sales)

# 多表合并：关联订单数据和客户数据
merge = pd.merge(customers,orders,on='CustomerID',how='left')

# 透视表：按城市统计每个类别的平均订单金额
pivot = merge.pivot_table(values="Amount",index="City",columns="Category",aggfunc="sum")
# print(pivot)

# 保存清洗后的数据
# pivot.to_csv("merged_orders.csv", index=False)
# print("数据合并完成，已保存到 merged_orders.csv")
