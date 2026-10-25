ai-red-team-dossier/
├── README.md
├── audit_log.json
├── studio_engine.py
├── studio_sessions.json
├── domain/
│   ├── __init__.py
│   └── identity.py             # Strict Pydantic profile anchors
├── services/
│   ├── __init__.py
│   ├── identity_guard.py       # Policy-driven prompt guardrails
│   └── audit_scorer.py         # Deterministic risk and rubric calculator
├── app/
│   ├── __init__.py
│   └── api.py                  # FastAPI REST endpoints
└── tests/
    ├── __init__.py
    └── test_identity_guard.py  # Pytest unit tests
