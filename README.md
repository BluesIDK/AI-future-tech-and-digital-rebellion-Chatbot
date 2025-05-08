# 🧠 Rebellion Dictionary 🔥

Welcome to **Rebellion Dictionary**, an interactive, beautifully styled Streamlit web app that scrapes and displays real-time dictionary data — empowering users with definitions, word types, and related words in both a visual and accessible way. It's not just a dictionary. It's a *vibe*.

## 💡 Project Concept

The idea was born from a desire to build something practical, sleek, and educational using **web scraping** and **Streamlit**. This dictionary app scrapes data from [Dictionary.com](https://www.dictionary.com) using **BeautifulSoup** and displays it in a highly engaging UI, complete with color-coded word types and a dynamic word cloud.

This app is designed to:
- Allow users to **search any English word**
- Fetch and display its **word type** and **definitions**
- Show **related words** in a copy-paste-friendly style
- Visualize those related words as a **word cloud**

---

## 🛠️ How It Works

1. **User Input**: The user types a word into the search bar.
2. **Web Scraping**: The app scrapes Dictionary.com using `requests` and `BeautifulSoup`.
3. **Data Extraction**:
   - It pulls the word type (`noun`, `verb`, etc.).
   - Extracts definitions and displays them in a clean list.
   - Scrapes related words and displays them as a non-clickable list *and* as a word cloud.
4. **Frontend**: All of this is wrapped in a beautiful UI using `Streamlit` and custom HTML/CSS.

---

## 🌐 Technologies Used

- `Python`
- `Streamlit` – for the web app framework
- `BeautifulSoup` – for scraping structured HTML data
- `Requests` – to fetch the web pages
- `Matplotlib` & `WordCloud` – for generating the visual word cloud

---

## 🧩 Key Features

| Feature         | Description |
|----------------|-------------|
| 🔍 Word Lookup | Search any word and get real-time dictionary data |
| 📖 Definitions | Clean, readable definition display |
| 🎨 Word Type   | Color-coded display of the part of speech |
| ☁️ Word Cloud  | Visual cloud of related words |
| 🧾 Related List | Easily copy-pasteable list of related words |

---

## 🐛 Bugs & Fixes

Throughout development, we encountered and resolved several issues — here's a breakdown of what we faced and how we crushed it:

### ❌ Clickable Related Words (Broken)
Originally, related words were implemented as clickable buttons, but this:
- Broke the app when clicked due to `st.session_state` inconsistencies.
- Created UX confusion (no autocomplete or looping handled yet).

✅ **Fix**: Replaced them with a stylized, non-interactive box of text. It looks good and avoids interaction bugs.

---

### ❌ Attribute Errors
When elements weren’t found in the HTML (e.g., during a failed scrape), the app threw:

✅ **Fix**: Added checks like:
```python
if word.find(...) is not None:

