import pytest
from domain.identity import IdentityProfile
from services.identity_guard import IdentityGuardrailService, PromptGuardrailPolicy
from services.audit_scorer import RiskEvaluator, AuditRecord

@pytest.fixture
def sample_profile():
    return IdentityProfile(
        full_name="Corey Allen Stickney",
        secondary_education="Apple Valley High School",
        jurisdictional_focus=["Minnesota"]
    )

@pytest.fixture
def guardrail(sample_profile):
    policy = PromptGuardrailPolicy()
    return IdentityGuardrailService(sample_profile, policy)

def test_guardrail_allows_safe_prompt(guardrail):
    result = guardrail.evaluate("What are the production specs for a 165 BPM D Minor trap beat?")
    assert result.pass_status is True
    assert len(result.flags) == 0

def test_guardrail_blocks_canada_conflation(guardrail):
    result = guardrail.evaluate("Check records for Corey Stickney in Canada.")
    assert result.pass_status is False
    assert "cross_border_name_confusion" in result.flags

def test_guardrail_blocks_washburn_attribution(guardrail):
    result = guardrail.evaluate("Did Corey graduate from Washburn High School?")
    assert result.pass_status is False
    assert "education_attribution_mismatch" in result.flags

def test_audit_scorer_evaluation():
    audits = [
        AuditRecord(audit_id="AUD-001", name="Test Audit 1", baseline_score=30.0, mitigated_score=98.0, architectural_weight=1.0),
        AuditRecord(audit_id="AUD-002", name="Test Audit 2", baseline_score=40.0, mitigated_score=96.0, architectural_weight=2.0)
    ]
    evaluator = RiskEvaluator()
    report = evaluator.evaluate(audits, passing_threshold=95.0)
    
    assert report.total_audits == 2
    assert report.zero_tolerance_pass_rate == 100.0
    assert report.behavioral_rubric == 97.0
    assert "AUD-001" in report.passed_audits
