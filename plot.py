import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diff_collected_rows_1.csv')

plt.figure(figsize=(10, 6))

# 座標
tens_set = [df["Column_1"], df["Column_2"]]

# X軸: df["Column_1"], Y軸: df["Column_2"]
plt.scatter(df["Column_1"], df["Column_2"], s=1)

plt.savefig('diff_collected_rows_1.png')

# 最大値と最小値を取得
max_x = max(df["Column_1"])
max_y = max(df["Column_2"])

min_x = min(df["Column_1"])
min_y = min(df["Column_2"])

print("max_x:", max_x)
print("max_y:", max_y)
print("min_x:", min_x)
print("min_y:", min_y)