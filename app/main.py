from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.processor import process_transcript_to_slides
import os
import nltk

# 1. Define a local directory for NLTK data
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

# 2. Tell NLTK to use this path
nltk.data.path.append(nltk_data_path)

# 3. Download to that specific path
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)

app = FastAPI()

class TranscriptInput(BaseModel):
    transcript: str

@app.post("/generate-slides")
async def generate_slides(data: TranscriptInput):
    if not data.transcript.strip():
        raise HTTPException(status_code=400, detail="Transcript is empty")
    
    try:
        # Run the logic and return response immediately
        result = process_transcript_to_slides(data.transcript)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "active"}
