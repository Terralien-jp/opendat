# datファイルは同じディレクトリに置く
file_name = "1646474056.dat.txt"
# ファイル名をJISコードで開く
with open(file_name, encoding="cp932") as f:
    data_lines = f.read()

# 文字列置換　Datからコピペ　そのうち曜日判定など改修予定
data_lines = data_lines.replace("2022/03/04 ", "2022/03/04(金)")

# ファイル名から余計な.txtを外して保存
with open(file_name.replace('.txt', ''), mode="w", encoding="cp932") as f:
    f.write(data_lines)