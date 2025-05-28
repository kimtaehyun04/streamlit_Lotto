import streamlit as st
import random
from datetime import datetime

st.title('로또 번호')
st.header('로또 번호를 생성합니다.')

def genlotto():
    lotto = set()
    while(len(lotto)<6):
        number = random.randint(1, 46)
        lotto.add(number)
    return list(lotto)

button = st.button('생성하기')
reset = st.button('리셋하기기')

if button:
    #랜덤 숫자 6개 생성
    for i in range(1, 7):
        numbers = genlotto()
        st.subheader(f':material/Settings: 번호{i}: :orange[{numbers}]')
    #time
    st.write('시간: ', datetime.now().strftime('%Y-%m-%d %H:%M'))

if reset:
    st.rerun()