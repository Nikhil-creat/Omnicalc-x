# OmniCalc-X — Starter Scaffold

**Designed and Developed by Nikhil Chary Sriramoju**
GitHub: [github.com/Nikhil-creat](https://github.com/Nikhil-creat) · LinkedIn: [in/nikhil-chary-sriramoju](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a) · Email: nikhilsriramoju66@gmail.com

This is a **working starting skeleton**, not the finished platform described
in the spec. Every service boots, has a `/health` endpoint, and the pieces
are wired together — but the actual intelligence (the CNN weights, the
vector index, the real agent prompts) is left as `TODO`s for you to fill in.
Building the full "production-grade autonomous scientific supercomputing
platform" as literally described is a multi-quarter, multi-engineer effort;
this gives you a real foundation to build on incrementally instead of an
unusable wall of speculative code.

## Layout

```
omnicalc-x/
├── docker-compose.yml          # orchestrates all 5 services
├── frontend/                   # Next.js app (KaTeX rendering, problem input)
├── api-gateway/                # FastAPI: REST + WebSocket, routes to the others
│   └── app/
│       ├── routers/solve.py    # POST /api/solve -> agent-orchestrator
│       ├── routers/ingest.py   # POST /api/ingest/image -> vision-service
│       └── core/config.py
├── vision-service/             # CNN/OCR formula recognition (stubbed model)
│   └── app/pipeline/ofr_pipeline.py
├── vector-db/                  # Qdrant (off-the-shelf image, no code needed)
├── agent-orchestrator/         # Planner -> Executor -> Verifier -> Synthesizer
│   └── app/
│       ├── agents/             # one file per agent
│       ├── graphs/reasoning_graph.py
│       └── state/reasoning_state.py
└── README.md
```

## Running it

```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- API gateway: http://localhost:8000/health
- Vector DB (Qdrant): internal only, reachable from other containers at
  `http://vector-db:6333`

## What's real vs. stubbed

| Piece | Status |
|---|---|
| Service wiring, Docker networking, health checks | Real |
| FastAPI routes, WebSocket session endpoint | Real (return stub data) |
| Agent pipeline control flow (plan → execute → verify → synthesize) | Real, sequential |
| CNN/Transformer model for handwriting → LaTeX | **Stub** — no weights, `_infer()` raises `NotImplementedError` |
| Vector DB content (papers, constants, tables) | **Empty** — Qdrant runs but has no collections yet |
| LLM calls inside each agent | **Stub** — replace the `TODO`s with real API calls |
| Sandboxed code execution for the Execution agent | **Stub** — do not wire this to raw `eval()`; use a real restricted runtime |

## Suggested build order

1. Get `api-gateway` → `agent-orchestrator` → back to frontend working
   end-to-end with stubbed text (no vision, no RAG) so you have a demo-able
   loop.
2. Add a real LLM call in each agent (planner/executor/verifier/synthesizer).
3. Stand up a Qdrant collection and wire real retrieval into the planner's
   context.
4. Only then tackle the vision pipeline — it's the most expensive piece
   (needs a trained or fine-tuned model) and isn't required for the other
   three subsystems to work.

## Roadmap — futuristic / stretch features

These aren't built yet, but the architecture leaves room for them:

- **Real-time collaborative whiteboard** — multiple users solving the same
  problem together over the existing WebSocket session channel (CRDT-based
  sync of canvas strokes and agent output).
- **Voice-driven problem input** — speech-to-formula, so a user can dictate
  "integral of x squared from 0 to 1" and have it parsed the same way an
  image capture is.
- **AR overlay mode** — point a phone camera at a printed textbook problem;
  the vision-service pipeline recognizes it live and overlays the solved
  steps in-frame.
- **Federated/on-device inference** — a distilled version of the vision
  model that runs client-side (ONNX.js / WebGPU) for offline formula
  recognition, falling back to the server model for low-confidence cases.
- **Self-improving verifier** — log every Verifier agent rejection and
  periodically fine-tune the Execution agent's prompting/tools against
  that rejection log (a lightweight RLHF-style loop, not full retraining).
- **Multi-modal RAG expansion** — ingest lecture video transcripts and
  textbook diagrams into the vector store, not just text/proofs.
- **Plugin API for domain packs** — let the Agent Squad load
  domain-specific tool sets (e.g. a circuits pack, a genomics pack) without
  redeploying the orchestrator.
- **Usage analytics dashboard** — surface the OpenTelemetry traces (token
  spend, latency, retrieval relevance) already planned in Section 2 as a
  real Grafana/Next.js dashboard instead of raw traces.

None of these are required to get the current scaffold running — they're
here as a backlog for whoever picks this project up next.

---

*OmniCalc-X — designed and developed by Nikhil Chary Sriramoju.*
