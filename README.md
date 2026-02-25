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

## 🧠 The Algorithms: How it Works

The intelligence of this API relies on two distinct Natural Language Processing (NLP) pillars:

### 1. Latent Semantic Analysis (LSA)
LSA acts as the **"Big Picture Analyst."** It identifies hidden (latent) relationships between words to understand the core themes of your transcript.
* **Mechanism:** Uses **Singular Value Decomposition (SVD)** to build a matrix of words and documents, compressing it to find the underlying concept structure.
* **Benefit:** Recognizes synonyms and context, ensuring that the most representative sentences are selected for bullets even if the phrasing varies.
* **Role:** Powers the **bullet point generation**.



### 2. YAKE! (Yet Another Keyword Extractor)
YAKE! is the **"Precision Hunter."** It is a light, unsupervised tool that extracts key phrases from a single piece of text without needing massive background datasets.
* **Mechanism:** Evaluates words based on five statistical features: **Casing** (capitalization), **Word Position**, **Frequency**, **Context Relatedness**, and **Dispersion**.
* **Benefit:** Extremely fast and doesn't require a pre-trained corpus.
* **Role:** Identifies the **Slide Titles** by ranking the most significant phrases.

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