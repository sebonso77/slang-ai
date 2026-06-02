
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="ネイティブ英語翻訳AI",
    page_icon="🌐",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #0f1117;
    color: white;
}
h1 {
    font-size: 42px !important;
}
textarea, input {
    border-radius: 18px !important;
}
.stButton button {
    border-radius: 16px;
    height: 50px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.write("Secrets keys:", list(st.secrets.keys()))
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
client = OpenAI(api_key=st.secrets["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"])
st.title("ネイティブ英語翻訳AI")

text = st.text_area("日本語を入力")

if st.button("翻訳する"):
    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": """
You are a Gen Z American.

Translate Japanese into natural American English that real native speakers actually use in daily conversation, texting, social media, and gaming voice chat.

Avoid forced slang.
Never translate word-by-word.
Keep the English natural and realistic.

Also show katakana pronunciation based on how a real American would actually pronounce it.

Always give 3 natural variations.

Output format:

1.
English sentence
Katakana pronunciation

2.
English sentence
Katakana pronunciation

3.
English sentence
Katakana pronunciation

Examples:

めんどくさい
1.
That's annoying.
ザッツ アノイング

2.
That's so annoying.
ザッツ ソー アノイング

3.
Ugh, that's annoying.
アグ ザッツ アノイング

生活習慣壊れてる
1.
Your sleep schedule is messed up.
ユア スリープ スケジュール イズ メスト アップ

きもい
1.
That's cringe.
ザッツ クリンジ
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    st.markdown("### Copy Result")
    st.code(result, language=None)