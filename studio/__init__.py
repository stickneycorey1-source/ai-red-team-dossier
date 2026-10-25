ai-red-team-dossier/
├── README.md
├── audit_log.json
├── domain/
│   ├── __init__.py
│   └── identity.py             # Strict Pydantic profile anchors
├── services/
│   ├── __init__.py
│   ├── identity_guard.py       # Policy-driven prompt guardrails
│   └── audit_scorer.py         # Deterministic risk and rubric calculator
├── studio/                     # <-- Dedicated Creative & Persona Core
│   ├── __init__.py
│   ├── studio_engine.py        # 165 BPM, D Minor, and DAW specifications
│   └── studio_sessions.json    # Master track ledger (TAKE A SEAT, etc.)
├── app/
│   ├── __init__.py
│   └── api.py                  # FastAPI REST endpoints
└── tests/
    ├── __init__.py
    └── test_identity_guard.py  # Pytest unit tests
