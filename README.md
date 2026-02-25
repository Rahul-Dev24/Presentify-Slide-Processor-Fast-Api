# 🚀 AI Transcript to Slide Generator

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

An ultra-fast, production-grade API that transforms long video transcripts into structured, presentation-ready slide content. Using **Natural Language Processing (NLP)**, it cleans filler words, identifies core concepts, and generates bulleted summaries.

---

## ✨ Key Features

* **⚡ High Performance:** Built with FastAPI and Uvicorn for asynchronous request handling.
* **🧠 Intelligent Summarization:** Uses LSA (Latent Semantic Analysis) to extract the most impactful sentences.
* **🏷️ Smart Titling:** Automatically detects Nouns and Proper Nouns to create meaningful slide titles.
* **🧹 Auto-Cleaning:** Filters out common video filler words like "subscribe," "welcome back," and "thanks for watching."
* **🚀 Deployment Ready:** Optimized for Render with pre-cached NLTK data for instant responses.

---

## 📂 Project Structure

```text
transcript-processor/
├── app/
│   ├── main.py          # API Routes & FastAPI Setup
│   ├── processor.py     # NLP Logic & Summarization Engine
│   └── schemas.py       # Pydantic Data Models
├── build.sh             # Production Build Script
├── requirements.txt     # Python Dependencies
└── README.md            # You are here!