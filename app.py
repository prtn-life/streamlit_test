import pandas as pd
import streamlit as st

# タイトル
st.title("売上データの可視化")

# Excelファイルの読み込み
file_path = "data.xlsx"  # GitHubにアップロードされたExcelファイル
df = pd.read_excel(file_path)

# グラフの描画
st.line_chart(df["売上"])

# データ全体を表示
st.write("データプレビュー", df)
