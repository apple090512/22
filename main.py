import streamlit as st

# 드라마 추천 데이터 (간단한 예시)
drama_data = {
    "로맨스": ["사랑의 불시착", "도깨비", "그 해 우리는", "이태원 클라쓰"],
    "스릴러": ["시그널", "악의 꽃", "보이스", "비밀의 숲"],
    "코미디": ["김비서가 왜 그럴까", "쌈, 마이웨이", "힘쎈여자 도봉순"],
    "역사/사극": ["미스터 션샤인", "해를 품은 달", "육룡이 나르샤"],
    "판타지": ["호텔 델루나", "도깨비", "W", "알함브라 궁전의 추억"]
}

# Streamlit 앱 타이틀
st.title("🎬 장르 기반 드라마 추천기")

# 사용자로부터 장르 선택 받기
genre = st.selectbox("장르를 선택하세요:", list(drama_data.keys()))

# 추천 드라마 출력
st.subheader(f"📺 {genre} 장르 추천 드라마:")
for drama in drama_data[genre]:
    st.write(f"- {drama}")
