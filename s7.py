import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지? 간식 추천기", page_icon="😋", layout="centered")

# 제목과 소개
st.title("✨ 오늘 뭐 먹지? 맞춤형 간식 추천기 ✨")
st.markdown("지금 내 기분과 입맛에 딱 맞는 간식을 골라줄게! 아래에서 골라봐.")

# 카테고리 정의
categories = {
    "💥 스트레스 만땅! (달달/짜릿)": ["탕후루", "초콜릿 케이크", "마카롱", "꾸덕한 브라우니", "도넛"],
    "🥱 입이 심심해~ (바삭/가볍)": ["감자칩", "나쵸와 치즈소스", "팝콘", "고구마 스틱", "러스크"],
    "🔥 매콤/짭짤한 게 당겨! (자극적)": ["국물 떡볶이", "닭강정", "불닭볶음면", "타코야끼", "소시지"],
    "🌿 건강도 챙겨야지... (부담 제로)": ["요거트 보울", "방울토마토", "구운 계란", "곤약 젤리", "단호박 칩"],
    "🧊 시원하게 가고 싶다 (속 뻥 뚫림)": ["소프트아이스크림", "팥빙수", "과일 소르베", "아이스 아메리카노", "스무디"]
}

# 사용자 선택 (셀렉트박스)
choice = st.selectbox("👉 지금 당신의 상태는?", list(categories.keys()))

# 추천 버튼
if st.button("🔮 간식 추천받기", type="primary"):
    selected_snack = random.choice(categories[choice])
    
    # 결과 출력 디자인
    st.balloons() # 축하 풍선 효과!
    st.success(f"오늘의 추천 간식은 바로... **[{selected_snack}]**!!")
    st.markdown("고민은 배송을 늦출 뿐! 맛있게 먹고 행복한 하루 보내자구 😋")
