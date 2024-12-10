import pandas as pd
import streamlit as st

# タイトル
st.title("売上データの推移")

# Excelファイルの読み込み
file_path = "data.xlsx"  # GitHubにアップロードされたExcelファイル
df = pd.read_excel(file_path)

# 日付列を日時型に変換
df["日付"] = pd.to_datetime(df["日付"])

# 指定された期間のデータをフィルタリング
filtered_df = df[(df["日付"] >= "2024-12-01") & (df["日付"] <= "2024-12-03")]

# フィルタリングしたデータを表示
st.write("指定期間のデータ", filtered_df)

# グラフの描画
st.line_chart(filtered_df.set_index("日付")["売上"])
