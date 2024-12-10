import streamlit as st

st.title("Hello, Streamlit!")
st.write("これはとても簡単な Streamlit アプリです！")
file_buffer = st.file_uploader("ファイルをアップロードしてください")
