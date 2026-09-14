from fastapi import APIRouter, UploadFile
from pydantic import BaseModel

router = APIRouter()


class IngestResponse(BaseModel):
    image_ref: str
    latex: str | None = None
    ast: dict | None = None


@router.post("/image", response_model=IngestResponse)
async def ingest_image(file: UploadFile) -> IngestResponse:
    """
    Forwards an image (handwritten formula, matrix, chemical schematic) to
    vision-service for OFR (optical formula recognition) and returns the
    parsed LaTeX / AST representation.
    """
    # TODO: stream file bytes to vision-service, parse response
    return IngestResponse(image_ref="stub-ref", latex=None, ast=None)
