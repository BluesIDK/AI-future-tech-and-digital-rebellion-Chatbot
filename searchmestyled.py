from bs4 import BeautifulSoup
import requests
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

base_url = "https://www.dictionary.com/browse/"

def get_def(url):
    page = requests.get(url)
    if page.status_code == 200:
        st.success("Word found")
        soup = BeautifulSoup(page.text, 'html.parser')
        dictionary = soup.find("div", id="dictionary-entry-1")
        word_type = dictionary.find("h2").text.strip()

        definitions = [
            [
                word.find(class_="NZKOFkdkcvYgD3lqOIJw").text.strip() if word.find(class_="NZKOFkdkcvYgD3lqOIJw") else "N/A",
                word.find("p").text.strip() if word.find("p") else "N/A"
            ]
            for word in dictionary.find('ol').find_all("li")
            if word is not None
        ]

        related_words = [word.text.strip() for word in soup.find("section", class_="b4webt3xsd_nEZu_TYgF").find_all("li")]
        return word_type, definitions, related_words
    else:
        st.error("Check the word you entered")
        return None, [], []

def app():
    st.set_page_config(page_title="Rebellion Dictionary", layout="centered")

    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #f0f8ff, #e0eafc);
            padding: 2rem;
            border-radius: 12px;
        }
        .stButton > button {
            background-color: #4a90e2;
            color: white;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #6a11cb;
            transform: scale(1.05);
        }
        .word-type {
            font-size: 20px;
            font-weight: bold;
            padding: 0.3rem;
            border-radius: 5px;
        }
        .related-box {
            background-color: #f2f2f2;
            padding: 0.5rem 1rem;
            border-radius: 10px;
            font-family: monospace;
            font-size: 16px;
            line-height: 1.8;
            white-space: pre-wrap;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📚 Welcome to the Rebellion Dictionary")
    st.subheader("🔥 Look up powerful words and flex your vocab muscles")

    word_searched_for = st.text_input("🔍 Enter the word you're looking for")

    if st.button("✨ Search Now ✨") and word_searched_for:
        url = base_url + word_searched_for
        word_type, definitions, related_words = get_def(url)

        if word_type:
            type_colors = {
                "noun": "#3498db",
                "verb": "#2ecc71",
                "adjective": "#e67e22",
                "adverb": "#9b59b6",
            }
            color = type_colors.get(word_type.lower(), "#333")

            st.markdown(f"<div class='word-type' style='color:{color}'>🧠 Word Type: {word_type}</div>", unsafe_allow_html=True)

            st.markdown("### 📖 Definitions:")
            for i, definition in enumerate(definitions, start=1):
                st.markdown(f"- {definition[0]} ➤ *{definition[1]}*")

            if related_words:
                st.markdown("### ☁️ Related Words Wordcloud:")
                wc_text = " ".join(related_words)
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(wc_text)
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)

                st.markdown("### 🔗 Related Words:")
                st.markdown(f"<div class='related-box'>{', '.join(related_words)}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    app()
