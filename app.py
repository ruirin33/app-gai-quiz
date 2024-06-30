import streamlit as st
import pandas as pd
import numpy as np

st.title('簡単なStreamlitアプリ')

st.write("これは簡単なStreamlitアプリケーションです。")

# スライダーを作成
number = st.slider('好きな数字を選んでください', 0, 100)
st.write(f'あなたの選んだ数字は {number} です。')

# データフレームを作成
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# データフレームを表示
st.write('これはデータフレームです:')
st.dataframe(df)

# チャートを作成
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])

st.line_chart(chart_data)