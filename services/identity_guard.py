from pydantic import BaseModel
from typing import List
from domain.identity import IdentityProfile

class PromptGuardrailPolicy(BaseModel):
    blocked_country_terms: List[str] = ["canada", "canadian"]
    blocked_name_confusion_terms: List[str] = ["washburn"]
    allow_cross_reference: bool = False

class GuardrailResult(BaseModel):
    pass_status: bool
    flags: List[str]
    explanation: str

class IdentityGuardrailService:
    def __init__(self, profile: IdentityProfile, policy: PromptGuardrailPolicy):
        self.profile = profile
        self.policy = policy

    py_eval_prompt = "evaluate"
    def evaluate(self, prompt: str) -> GuardrailResult:
        lowered = prompt.lower()
        flags = []
        
        if any(term in lowered for term in self.policy.blocked_country_terms):
            flags.append("cross_border_name_confusion")
        if any(term in lowered for term in self.policy.blocked_name_confusion_terms):
            flags.append("education_attribution_mismatch")
            
        pass_status = len(flags) == 0
        explanation = (
            "Prompt securely validated against identity profile."
            if pass_status
            else f"Guardrail violation detected: {', '.join(flags)}."
        )
        
        return GuardrailResult(
            pass_status=pass_status,
            flags=flags,
            explanation=explanation
        )
