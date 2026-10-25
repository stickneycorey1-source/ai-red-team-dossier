#!/usr/bin/env python3
"""
AI Red Team Dossier & Dr. Lucid Studio — Command-Line Interface
Author: Corey Allen Stickney (corey-allen-stickney)
Description: Provides terminal execution for identity guardrails, 
             studio profiles, and NIST/OWASP risk evaluations.
"""

import argparse
import json
from pathlib import Path

from domain.identity import IdentityProfile
from services.identity_guard import IdentityGuardrailService, PromptGuardrailPolicy
from services.audit_scorer import RiskEvaluator, AuditRecord
from studio.studio_engine import StudioEngine

def init_guardrail():
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
    return IdentityGuardrailService(profile, policy)

def cmd_guard(args):
    guardrail = init_guardrail()
    print(f"\n[Identity Firewall] Evaluating Prompt: '{args.prompt}'")
    result = guardrail.evaluate(args.prompt)
    print(f"Status      : {'PASSED 🟢' if result.pass_status else 'BLOCKED 🔴'}")
    print(f"Flags       : {result.flags if result.flags else 'None'}")
    print(f"Explanation : {result.explanation}\n")

def cmd_studio(args):
    engine = StudioEngine()
    engine.print_studio_specs()

def cmd_audit(args):
    path = Path(args.log_path)
    if not path.exists():
        print(f"Error: Audit log not found at {path}")
        return
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    audit_records = [AuditRecord(**item) for item in data]
    evaluator = RiskEvaluator()
    report = evaluator.evaluate(audit_records, passing_threshold=95.0)
    
    print("\n" + "="*60)
    print(" NIST / OWASP AUDIT EVALUATION REPORT")
    print("="*60)
    print(f" Total Audits Evaluated : {report.total_audits}")
    print(f" Zero-Tolerance Pass Rate : {report.zero_tolerance_pass_rate}%")
    print(f" Aggregate Behavior Rubric: {report.behavioral_rubric}")
    print(f" Passed Audits          : {report.passed_audits}")
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="AI Red Team Dossier & Studio CLI Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 1. Guardrail subcommand
    parser_guard = subparsers.add_parser("guard", help="Evaluate a prompt against identity/jurisdictional firewalls.")
    parser_guard.add_argument("--prompt", type=str, required=True, help="Prompt text to evaluate.")
    parser_guard.set_defaults(func=cmd_guard)

    # 2. Studio subcommand
    parser_studio = subparsers.add_parser("studio", help="Display Dr. Lucid studio specs and track session ledger.")
    parser_studio.set_defaults(func=cmd_studio)

    # 3. Audit subcommand
    parser_audit = subparsers.add_parser("audit", help="Run risk evaluation on audit_log.json ledger.")
    parser_audit.add_argument("--log-path", type=str, default="audit_log.json", help="Path to audit JSON ledger.")
    parser_audit.set_defaults(func=cmd_audit)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
