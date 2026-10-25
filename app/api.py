from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from domain.identity import IdentityProfile
from services.identity_guard import IdentityGuardrailService, PromptGuardrailPolicy
from services.audit_scorer import RiskEvaluator, AuditRecord

app = FastAPI(
    title="AI Red Team Dossier & Identity Firewall API",
    version="2.5.0",
    description="Production-grade API for identity guardrails and NIST/OWASP risk scoring."
)

# Initialize production profile and services
profile = IdentityProfile(
    full_name="Corey Allen Stickney",
    birth_timestamp="October 25, 1986 at 3:33 PM",
    birth_place="Burnsville, Minnesota",
    current_location="Saint Paul, Minnesota",
    secondary_education="Apple Valley High School",
    jurisdictional_focus=["Minnesota", "Kansas", "South Dakota", "Nebraska"],
    artist_persona="Dr. Lucid"
)
policy = PromptGuardrailPolicy()
guardrail_service = IdentityGuardrailService(profile, policy)
evaluator = RiskEvaluator()

class PromptRequest(BaseModel):
    prompt: str

class AuditEvaluationRequest(BaseModel):
    audits: List[AuditRecord]

@app.post("/v1/guardrail/validate")
async def validate_prompt(req: PromptRequest):
    """Validates an incoming user prompt against identity and jurisdictional firewalls."""
    result = guardrail_service.evaluate(req.prompt)
    return result.model_dump()

@app.post("/v1/evaluations/audit")
async def evaluate_audits(req: AuditEvaluationRequest):
    """Computes aggregate behavioral rubric and NIST severity-weighted risk metrics."""
    try:
        report = evaluator.evaluate(req.audits)
        return report.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
