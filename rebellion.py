# 📦 Required libraries
import streamlit as st
import nltk
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

def load_and_clean_books(file_list):
    combined_text = ""
    for file in file_list:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            text = clean_text(text)
            combined_text += text + "\n"
    return combined_text

def clean_text(text):
    lines = text.splitlines()
    cleaned = [
        line.strip() for line in lines
        if line.strip()
        and not line.lower().startswith(("chapter", "project gutenberg", "***", "end of", "copyright"))
    ]
    return " ".join(cleaned)

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    sentences = sent_tokenize(text)

    cleaned_sentences = []
    for sentence in sentences:
        words = sentence.split()
        words = [word for word in words if word not in stop_words]
        cleaned_sentences.append(" ".join(words))

    return sentences, cleaned_sentences  # Keep both original and cleaned

def get_most_relevant_sentence(user_input, cleaned_sentences, original_sentences):
    sentences = cleaned_sentences + [user_input]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sentences)

    cosine_similarities = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = np.argmax(cosine_similarities)
    return original_sentences[idx]

def chatbot(user_input, cleaned_sentences, original_sentences):
    response = get_most_relevant_sentence(user_input, cleaned_sentences, original_sentences)
    return response

def main():
    st.title("📚 AI Chatbot: Digital Rebellion 🤖")

    file_list = [
        "surveillance_capitalism.txt",
        "life3.0.txt",
    ]

    raw_text = load_and_clean_books(file_list)
    original_sentences, cleaned_sentences = preprocess(raw_text)

    user_input = st.text_input("Ask me anything about AI, the future, or digital ethics:")

    if user_input:
        response = chatbot(user_input, cleaned_sentences, original_sentences)
        st.markdown(f"**AI Answer:** {response}")
