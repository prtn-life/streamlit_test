import pandas as pd
import streamlit as st
import plotly.express as px

# タイトル
st.title("売上データの推移 (棒グラフ: 日単位)")

# Excelファイルの読み込み
file_path = "data.xlsx"  # GitHubにアップロードされたExcelファイル
df = pd.read_excel(file_path)

# 日付列を日時型に変換
df["日付"] = pd.to_datetime(df["日付"])

# 指定された期間のデータをフィルタリング
filtered_df = df[(df["日付"] >= "2024-12-01") & (df["日付"] <= "2024-12-03")]

# フィルタリングしたデータを表示
st.write("指定期間のデータ", filtered_df)

# グラフの描画 (Plotlyで棒グラフを作成)
fig = px.bar(filtered_df, x="日付", y="売上", title="日単位の売上推移", labels={"日付": "日付", "売上": "売上金額"})
st.plotly_chart(fig)
