import streamlit as st
from openai import OpenAI

# ✅ API 키는 Streamlit secrets에서 안전하게 불러옵니다
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🎨 페이지 설정
st.set_page_config(page_title="AI 자기소개서 생성기", page_icon="📝", layout="centered")

# 🧾 상단 제목
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>✨ AI 자기소개서 생성기 ✨</h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>
        지원 정보를 입력하면, 인공지능이 문단별 자기소개서를 자동으로 작성해줍니다.
    </p>
    <hr style='margin-top: 20px; margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# 📥 입력 폼
job = st.text_input("📌 지원 직무를 입력하세요:")
strength = st.text_input("💪 나의 강점을 입력하세요:")
experience = st.text_area("📝 경험을 간단히 설명해 주세요:")

# 🚀 자기소개서 생성 버튼
if st.button("자기소개서 생성하기"):
    with st.spinner("AI가 자기소개서를 작성 중입니다..."):
        prompt = f"""
        다음 정보를 바탕으로 자기소개서를 작성해줘.
        문단은 다음 항목 순서로 구성해줘:
        1. 성장 과정
        2. 성격의 장단점
        3. 지원 동기
        4. 입사 후 포부

        요청사항:
        - 각 문단은 5~6줄 이상으로 상세히 작성해줘.
        - "저는", "저의", "제가"로 시작하는 문장은 피하고, 자연스럽고 다양한 표현을 사용해줘.
        - 문장 흐름이 부드럽고, 사례와 강점이 잘 드러나는 글로 작성해줘.

        입력 정보:
        지원 직무: {job}
        강점: {strength}
        경험: {experience}
        """

        # GPT 모델 호출
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

        # 결과 출력
        st.markdown("## 📝 생성된 자기소개서")
        st.write(result)

        # 📥 텍스트 다운로드 버튼
        st.download_button(
            label="📥 자기소개서 다운로드",
            data=result,
            file_name="자기소개서.txt",
            mime="text/plain"
        )
