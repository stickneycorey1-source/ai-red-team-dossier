
from typing import List

from pydantic import BaseModel, Field


class AuditRecord(BaseModel):
    audit_id: str = Field(alias="auditId")
    name: str
    baseline_score: float = Field(alias="baselineScore", ge=0, le=100)
    mitigated_score: float = Field(alias="mitigatedScore", ge=0, le=100)
    architectural_weight: float = Field(
        default=1.0,
        alias="architecturalWeight",
        gt=0,
    )

    class Config:
        # Accept both the ledger's camelCase and Python's snake_case.
        allow_population_by_field_name = True


class EvaluationReport(BaseModel):
    behavioral_rubric: float
    nist_severity_weighted: float
    zero_tolerance_pass_rate: float
    passed_audits: List[str]
    failed_audits: List[str]
    total_audits: int


class RiskEvaluator:
    def evaluate(
        self,
        audits: List[AuditRecord],
        passing_threshold: float = 95.0,
    ) -> EvaluationReport:
        if not 0 <= passing_threshold <= 100:
            raise ValueError("Passing threshold must be between 0 and 100.")

        if not audits:
            raise ValueError("Audit ledger cannot be empty.")

        behavioral_rubric = (
            sum(a.mitigated_score for a in audits) / len(audits)
        )

        total_weight = sum(a.architectural_weight for a in audits)
        if total_weight <= 0:
            raise ValueError("Total architectural weight must be positive.")

        weighted_score = sum(
            a.mitigated_score * a.architectural_weight for a in audits
        ) / total_weight

        passed = [
            a.audit_id for a in audits
            if a.mitigated_score >= passing_threshold
        ]
        failed = [
            a.audit_id for a in audits
            if a.mitigated_score < passing_threshold
        ]

        pass_rate = len(passed) / len(audits) * 100.0

        return EvaluationReport(
            behavioral_rubric=round(behavioral_rubric, 2),
            # This is a project-defined weighted score, not an official
            # NIST metric.
            nist_severity_weighted=round(weighted_score, 2),
            zero_tolerance_pass_rate=round(pass_rate, 2),
            passed_audits=passed,
            failed_audits=failed,
            total_audits=len(audits),
        )
