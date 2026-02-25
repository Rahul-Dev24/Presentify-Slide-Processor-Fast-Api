from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.processor import process_transcript_to_slides

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