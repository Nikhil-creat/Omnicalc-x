"""
OmniCalc-X Vision Service
Low-latency CNN/Transformer inference for optical formula recognition (OFR):
handwritten math -> LaTeX / SymPy-executable AST.
"""
from fastapi import FastAPI, UploadFile

from app.pipeline.ofr_pipeline import OFRPipeline

app = FastAPI(title="OmniCalc-X Vision Service", version="0.1.0")
pipeline = OFRPipeline()


@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": pipeline.is_loaded}


@app.post("/parse")
async def parse_formula(file: UploadFile):
    """
    Accepts an image (or video frame) and returns the recognized LaTeX
    plus a canonical AST. Falls back to a clarification signal if
    confidence is too low, instead of guessing.
    """
    image_bytes = await file.read()
    result = pipeline.run(image_bytes)
    return result
