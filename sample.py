import streamlit as st
st.markdown('### 三次元測定機 :sunglasses:')
x = st.slider('数値を選んでください',min_value=0, max_value=1000)
st.write(x, 'の三次元の値は：', x**3)
st.markdown('> Streamlitは便利です :+1:')
