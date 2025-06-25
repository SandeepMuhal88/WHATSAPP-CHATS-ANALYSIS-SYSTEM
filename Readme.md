    # 📊 WhatsApp Group Chat Analyzer – CSCYAIDS Edition

Ever wondered who talks the most in your group? Who sends the most emojis? When the late-night bakchodi peaks?  
Well, this project spills the digital tea! 🍵

> "From message overload to organized insights — this project turns chaos into clarity."

---

## 🚀 Project Summary

This project analyzes a **WhatsApp Group Chat (.txt export)** and extracts detailed insights using Python and NLP.  
Built using real chat data from the _"Unofficial 2022-26 CSCYAIDS"_ college group — because why analyze dummy data when you've got raw chaos to play with?

---

## 🎯 Features

- 📅 **Date & Time Analysis** — See when your group is most active.
- 👤 **Top Contributors** — Who spams, who lurks, who ghosts?
- 🔥 **Most Common Words/Emojis** — Let the true vibe reveal itself.
- 💬 **Message Timeline** — Track group activity across weeks/months.
- 📈 **Visualizations** — WordClouds, heatmaps, pie charts & more.
- 🧠 **Sentiment Analysis** — Who's positive, who's panicking before exams?
- 🤖 **Optional AI Integration** — Add GPT-style reply suggestions (coming soon).
- 📤 **Exportable Reports** — Share findings with your squad.

---

## 🛠️ Tech Stack

- **Python**
- `pandas` – for data wrangling  
- `matplotlib` / `seaborn` – for stunning plots  
- `re` – for regular expression parsing  
- `nltk` / `textblob` – for NLP  
- `wordcloud` – because visuals > words  
- `streamlit` – *(optional)* for interactive UI

---

## 📦 How to Use

1. Export your WhatsApp chat as `.txt` (without media).
2. Place it in the root folder.
3. Run the parser:
   ```bash
   python whatsapp_parser.py
