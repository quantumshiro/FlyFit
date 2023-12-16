import pandas as pd
import matplotlib.pyplot as plt
import math
import random

df = pd.read_csv('Sabun_diff_collected_rows_9.csv')

plt.figure(figsize=(10, 6))

# 座標
distances = [math.sqrt(abs(df["Column_1"][i] ** 2 - df["Column_2"][i] ** 2)) for i in range(len(df["Column_1"]))]
# print(distances)

# distancesにID(1...)をつける
distances = [(i+1, distances[i]) for i in range(len(distances))]

# 横軸: distancesのID, 縦軸: distancesの値
# distanceをサンプル抽出する
y = random.sample(distances, len(distances))

print(y)

plt.scatter([i[0] for i in y], [i[1] for i in y], s=1)
plt.savefig('Sabun_diff_collected_rows_9.png')