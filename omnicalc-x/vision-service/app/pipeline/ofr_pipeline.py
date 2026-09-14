"""
Optical Formula Recognition pipeline.

Replace `_load_model` / `_infer` with a real fine-tuned checkpoint
(a Donut/Nougat-style encoder-decoder is a reasonable starting point for
image-to-LaTeX). Keep the confidence-gated fallback: low-confidence
results should trigger a clarification dialogue in the agent layer
rather than returning a guess.
"""
from dataclasses import dataclass


CONFIDENCE_THRESHOLD = 0.6


@dataclass
class OFRResult:
    latex: str | None
    confidence: float
    needs_clarification: bool


class OFRPipeline:
    def __init__(self):
        self.model = None
        self.is_loaded = False
        self._load_model()

    def _load_model(self):
        # TODO: load checkpoint from MODEL_CACHE_DIR, move to GPU/ONNX runtime
        self.is_loaded = False  # flip true once a real model is wired in

    def run(self, image_bytes: bytes) -> OFRResult:
        if not self.is_loaded:
            return OFRResult(latex=None, confidence=0.0, needs_clarification=True)

        # TODO: preprocess -> model forward pass -> decode to LaTeX
        latex, confidence = self._infer(image_bytes)
        return OFRResult(
            latex=latex,
            confidence=confidence,
            needs_clarification=confidence < CONFIDENCE_THRESHOLD,
        )

    def _infer(self, image_bytes: bytes) -> tuple[str, float]:
        raise NotImplementedError
