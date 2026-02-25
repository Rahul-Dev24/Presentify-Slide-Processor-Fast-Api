import nltk
import yake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def process_transcript_to_slides(transcript: str):
    filler_words = {"video", "watching", "subscribe", "welcome", "guys", "hello", "thank", "next video"}
    
    # 1. Cleaning
    sentences = nltk.sent_tokenize(transcript)
    cleaned_sentences = [s for s in sentences if not any(w in s.lower() for w in filler_words)]
    
    # 2. Chunking
    chunk_size = 6
    chunks = [cleaned_sentences[i:i + chunk_size] for i in range(0, len(cleaned_sentences), chunk_size)]
    
    # 3. Processing
    kw_extractor = yake.KeywordExtractor(lan="en", n=2, top=5)
    summarizer = LsaSummarizer()
    slide_data = []
    
    for i, chunk in enumerate(chunks):
        chunk_text = " ".join(chunk)
        parser = PlaintextParser.from_string(chunk_text, Tokenizer("english"))
        important_sentences = summarizer(parser.document, 3)
        bullets = [str(s) for s in important_sentences]
        
        if not bullets: continue

        keywords = kw_extractor.extract_keywords(" ".join(bullets))
        best_title = "CORE CONCEPT"
        
        for kw_tuple in keywords:
            kw = kw_tuple[0]
            tokens = nltk.word_tokenize(kw)
            pos_tags = nltk.pos_tag(tokens)
            if any(tag.startswith('NN') for word, tag in pos_tags):
                best_title = kw.upper()
                break

        slide_data.append({
            "slide_index": i + 1,
            "title": best_title,
            "bullets": bullets
        })
        
    return slide_data