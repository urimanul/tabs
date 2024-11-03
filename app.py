import streamlit as st

# Streamlitアプリの設定
st.title('RAG')

# タブを作成
tabs = st.tabs(["LLM", "RAG", "PARSE"])

# タブ1の内容
with tabs[0]:
    st.header("タブ1の内容")
    st.write("ここにタブ1の内容を記述します。")

# タブ2の内容
with tabs[1]:
    st.header("タブ2の内容")
    st.write("ここにタブ2の内容を記述します。")

# タブ3の内容
with tabs[2]:
    st.header("タブ3の内容")
    st.write("ここにタブ3の内容を記述します。")
