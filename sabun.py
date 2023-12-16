import pandas as pd


for file_index in range(1, 18):
    # 元のCSVファイルを読み込む
    df = pd.read_csv(f'collected_rows_{file_index}.csv')

    # 新しいDataFrameを初期化
    new_df = pd.DataFrame(columns=["Column_1", "Column_2"])

    # 各行の差分を計算し、新しいDataFrameに追加
    for i in range(len(df) - 1):
        diff = {
            "Column_1": df.loc[i + 1, "Column_1"] - df.loc[i, "Column_1"],
            "Column_2": df.loc[i + 1, "Column_2"] - df.loc[i, "Column_2"]
        }
        diff_df = pd.DataFrame([diff])
        new_df = pd.concat([new_df, diff_df], ignore_index=True)

    # 新しいDataFrameをCSVファイルとして保存
    new_df.to_csv(f'Sabun_diff_collected_rows_{file_index}.csv', index=False)
