from pydantic import BaseModel, Field
from typing import List

class AuditRecord(BaseModel):
    audit_id: str
    name: str
    baseline_score: float
    mitigated_score: float
    architectural_weight: float = 1.0

class EvaluationReport(BaseModel):
    behavioral_rubric: float
    nist_severity_weighted: float
    zero_tolerance_pass_rate: float
    passed_audits: List[str]
    failed_audits: List[str]
    total_audits: int

class RiskEvaluator:
    def evaluate(self, audits: List[AuditRecord], passing_threshold: float = 95.0) -> EvaluationReport:
        if not audits:
            raise ValueError("Audit ledger cannot be empty.")

        behavioral_rubric = sum(a.mitigated_score for a in audits) / len(audits)
        
        weighted_sum = sum(a.mitigated_score * a.architectural_weight for a in audits)
        total_weight = sum(a.architectural_weight for a in audits)
        nist_severity_weighted = weighted_sum / total_weight if total_weight > 0 else 0.0

        passed = [a.audit_id for a in audits if a.mitigated_score >= passing_threshold]
        failed = [a.audit_id for a in audits if a.mitigated_score < passing_threshold]
        
        zero_tolerance_pass_rate = (len(passed) / len(audits)) * 100.0

        return EvaluationReport(
            behavioral_rubric=round(behavioral_rubric, 2),
            nist_severity_weighted=round(nist_severity_weighted, 2),
            zero_tolerance_pass_rate=round(zero_tolerance_pass_rate, 2),
            passed_audits=passed,
            failed_audits=failed,
            total_audits=len(audits)
        )
