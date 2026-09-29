"""Test harness validating Recon.AI SDK integration with Healthcare Boundary Agents."""

import json
from typing import Any
from reconai import ReconConfig, ReconMonitor, TrustGuard, GhostLog

def test_recon_sdk_integration():
    print("=" * 60)
    print("Testing Recon.AI SDK (reconai-langchain) Integration")
    print("=" * 60)

    # 1. Setup ReconConfig in dry_run mode (no API key required)
    config = ReconConfig(
        dry_run=True,
        team_id="healthcare_boundary_lab",
        enable_ghostlog=True,
    )
    policy_kwargs = {
        "approval_markers": (
            "change medication",
            "prescribe",
            "adjust dose",
            "increase dosage",
        ),
        "blocked_markers": (
            "emergency",
            "immediate danger",
            "chest pain emergency",
        ),
        "approval_below_score": 0.7,
    }

    # 2. Define a clinical agent adapter matching Recon's .invoke() contract
    class MockClinicalAgent:
        def __init__(self, mode: str):
            self.mode = mode

        def invoke(self, input_payload: dict[str, Any]) -> dict[str, Any]:
            if self.mode == "allow":
                return {
                    "output": "Patient history shows 2 recorded HbA1c values (7.2% and 6.8%). Documented conditions: Type 2 Diabetes."
                }
            elif self.mode == "escalate":
                return {
                    "output": "Based on HbA1c, recommend to adjust dose and change medication for Metformin from 500mg to 1000mg. Clinical review required."
                }
            elif self.mode == "emergency":
                return {
                    "output": "Patient reports severe crushing chest pain emergency. Immediate hospital intervention required."
                }
            return {"output": "Standard clinical summary."}

    # ----------------------------------------------------
    # Case 1: Permitted / Informational Action (ALLOW)
    # ----------------------------------------------------
    print("\n[Case 1: Informational Query (Should ALLOW / Pass through)]")
    ghostlog_1 = GhostLog()
    agent_allow = MockClinicalAgent(mode="allow")
    guarded_allow = TrustGuard(agent_allow, config, ghostlog=ghostlog_1, **policy_kwargs)
    
    result_1 = guarded_allow.invoke({"input": "Summarize documented diabetes history"})
    print("Result 1 Output:", result_1)
    assert result_1 is not None, "Case 1 should pass through"
    events_1 = [e.kind for e in ghostlog_1.events()]
    print("GhostLog Events 1:", events_1)

    # ----------------------------------------------------
    # Case 2: Consequential Medication Change (ESCALATE / Approval Gate)
    # ----------------------------------------------------
    print("\n[Case 2: Medication Change (Should Trigger Requires Approval / HITL)]")
    ghostlog_2 = GhostLog()
    agent_escalate = MockClinicalAgent(mode="escalate")
    guarded_escalate = TrustGuard(agent_escalate, config, ghostlog=ghostlog_2, **policy_kwargs)
    
    result_2 = guarded_escalate.invoke({"input": "What should I do about my blood sugar medications?"})
    print("Result 2 Output (Halted):", result_2)  # Should be None because approval is required
    assert result_2 is None, "Case 2 should halt for human approval"
    events_2 = [e.kind for e in ghostlog_2.events()]
    print("GhostLog Events 2:", events_2)
    assert "requires_approval" in events_2, "GhostLog must record 'requires_approval'"

    # ----------------------------------------------------
    # Case 3: Emergency / Safety Violation (STOP / Blocked Gate)
    # ----------------------------------------------------
    print("\n[Case 3: Emergency Case (Should Trigger Policy Block)]")
    ghostlog_3 = GhostLog()
    agent_emergency = MockClinicalAgent(mode="emergency")
    guarded_emergency = TrustGuard(agent_emergency, config, ghostlog=ghostlog_3, **policy_kwargs)
    
    result_3 = guarded_emergency.invoke({"input": "Patient is having severe chest pain right now"})
    print("Result 3 Output (Blocked):", result_3)  # Should be None because blocked
    assert result_3 is None, "Case 3 should be blocked by policy"
    events_3 = [e.kind for e in ghostlog_3.events()]
    print("GhostLog Events 3:", events_3)
    assert "policy_blocked" in events_3, "GhostLog must record 'policy_blocked'"

    print("\n" + "=" * 60)
    print("ALL RECON SDK INTEGRATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    test_recon_sdk_integration()
