import pandas as pd
import re
import torch


# テンソルデータをファイルから正しく読み込むための関数
def read_tensors(file_path):
    tensors = []
    current_tensor = []

    with open(file_path, 'r') as file:
        for line in file:
            # 余分な文字と空白を削除
            cleaned_line = re.sub(r'[^\d.,]', '', line).strip()
            if cleaned_line:
                # 数値を抽出して現在のテンソルに追加
                current_tensor += re.findall(r"[\d.]+", cleaned_line)
            else:
                # 現在のテンソルを座標ペアに変換してテンソルリストに追加
                if current_tensor:
                    tensor_pairs = [(float(current_tensor[i]), float(current_tensor[i+1])) for i in range(0, len(current_tensor), 2)]
                    tensors.append(tensor_pairs)
                    current_tensor = []

    # ファイルが空行で終わらない場合、最後のテンソルを追加
    if current_tensor:
        tensor_pairs = [(float(current_tensor[i]), float(current_tensor[i+1])) for i in range(0, len(current_tensor), 2)]
        tensors.append(tensor_pairs)

    return tensors

# ファイルからテンソルを読み込む
file_path = 'test.csv'
tensors = read_tensors(file_path)

# 各テンソルを17個の座標ごとに分割する
split_tensors = []
for tensor in tensors:
    for i in range(0, len(tensor), 17):
        split_tensors.append(tensor[i:i+17])

# 分割されたテンソルをテンソルオブジェクトに変換
split_tensors = [torch.tensor(tensor) for tensor in split_tensors]

# 分割されたテンソルの数と最初のテンソルを表示して確認
print("分割されたテンソルの数:", len(split_tensors))
print("最初の分割されたテンソル:", split_tensors[300])

# 各行をまとめてCSVに出力
num_rows = 17  # 各テンソルの行数（ここでは17と仮定）
for row_index in range(num_rows):
    collected_rows = []

    for tensor in split_tensors:
        if row_index < len(tensor):
            collected_rows.append(tensor[row_index].numpy().tolist())

    # DataFrameの作成
    df = pd.DataFrame(collected_rows, columns=[f'Column_{i+1}' for i in range(len(collected_rows[0]))])
    csv_file_path = f'collected_rows_{row_index+1}.csv'
    df.to_csv(csv_file_path, index=False)

    print(f'Row {row_index+1} collected to {csv_file_path}')
    
