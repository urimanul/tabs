import streamlit as st
import requests

# Streamlitアプリの設定
st.title('RAG')

# タブを作成
tabs = st.tabs(["LLM", "RAG", "PARSE"])

# タブ1の内容
with tabs[0]:
    st.header("LLM")
    llm_chain = st.text_area("プロンプトを入力して下さい", height=150, key="llm_chain")
    
    # Groq API設定
    API_URL = 'https://api.groq.com/openai/v1/'
    MODEL = 'Llama-3.1-70b-Versatile'
    API_KEY = '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'
    maxTokens = 4096
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # 生成ボタンの作成
    if st.button('生成'):
        data = {
            'model': MODEL,
            'max_tokens': maxTokens,
            'messages': [
                {
                    'role': 'system',
                    'content': '貴方は専門家です。できるだけわかりやすく答えてください。必ず、日本語で答えてください。'
                },
                {
                    'role': 'user',
                    'content': llm_chain
                }
            ]
        }
    
        response = requests.post(f'{API_URL}chat/completions', headers=headers, json=data)
        groqResp = response.json()['choices'][0]['message']['content']

        # 結果をsession_stateに保存
        st.session_state['groqResp'] = groqResp

    # 分析結果の表示
    if 'groqResp' in st.session_state:
        st.subheader('結果')
        st.text_area('Result', st.session_state['groqResp'], height=300)

# タブ2の内容
with tabs[1]:
    st.header("RAG")
    # ユーザー入力を取得
    rag_chain = st.text_area("プロンプトを入力してください")

    # APIキーとURLの設定
    apikey = 'GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg'
    url = 'https://api.cohere.com/v1/chat'
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json'
    }

    # ボタンが押されたときの処理
    if st.button("RAG生成"):
        # POSTデータを設定
        my_content = f"{rag_chain} 必ず、日本語で答えてください。"
        data = {
            "model": "command-r-plus",
            "message": rag_chain,
            "connectors": [{"id": "authryh-wfc54k"}, {"id": "o365schedule-e4baaa"}, {"id": "mental-health-r7n71k"}, {"id": "web-search"}]
        }

        # APIリクエストを送信
        response = requests.post(url, json=data, headers=headers)
        cohere_resp = response.json()
        #cohere_resp = str(response.json())
        #cohere_resp = response.json().get('text', 'No response')

        # 結果をsession_stateに保存
        st.session_state['cohere_resp'] = cohere_resp

    if 'cohere_resp' in st.session_state:
        st.subheader('結果')
        st.text_area('Result', st.session_state['cohere_resp'], height=300)

# タブ3の内容
with tabs[2]:
    st.header("タブ3の内容")
    st.write("ここにタブ3の内容を記述します。")
