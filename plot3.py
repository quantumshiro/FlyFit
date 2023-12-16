import pandas as pd
import matplotlib.pyplot as plt
import math
import random


for i in range(1, 18):
    plt.figure(figsize=(10, 6))
    # 元のCSVファイルを読み込む
    df = pd.read_csv(f'Sabun_diff_collected_rows_{i}.csv')
    distances = [math.sqrt(abs(df["Column_1"][i] ** 2 - df["Column_2"][i] ** 2)) for i in range(len(df["Column_1"]))]
    distances = [(i+1, distances[i]) for i in range(len(distances))]
    y = random.sample(distances, len(distances))
    plt.scatter([i[0] for i in y], [i[1] for i in y], s=1)
    plt.savefig(f'Sabun_diff_collected_rows_{i}.png')
