import streamlit as st

st.title("나의 첫 Streamlit 웹사이트")

st.write("안녕하세요! GitHub와 Streamlit 연결 성공!")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.success(f"{name}님, 반갑습니다!")
