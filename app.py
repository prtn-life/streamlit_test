import pandas as pd
import streamlit as st

# タイトルを設定
st.title("Excelデータを使った簡単グラフ")

# Excelファイルを読み込む
file_path = "data.xlsx"  # Excelファイルのパス
df = pd.read_excel(file_path)

# データを表示
st.write("データプレビュー", df)

# 折れ線グラフを表示
st.line_chart(df)

# 棒グラフを表示（オプション）
st.bar_chart(df["Sales"])
