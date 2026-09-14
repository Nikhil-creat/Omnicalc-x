"""
Reserved endpoints for the roadmap features described in the project
README (collaborative whiteboard, voice input, AR overlay, on-device
inference fallback, domain plugin packs). Each is a placeholder until
its subsystem is built — wiring them here now keeps the API surface
stable as they come online.
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/voice")
async def voice_input():
    """Speech-to-formula input. Not yet implemented."""
    return {"status": "not_implemented", "feature": "voice-driven problem input"}


@router.post("/collab/session")
async def start_collab_session():
    """Create a shared whiteboard session other users can join. Not yet implemented."""
    return {"status": "not_implemented", "feature": "collaborative whiteboard"}


@router.get("/plugins")
async def list_domain_plugins():
    """Lists installable domain packs (circuits, genomics, etc). Not yet implemented."""
    return {"status": "not_implemented", "feature": "plugin API for domain packs", "plugins": []}
