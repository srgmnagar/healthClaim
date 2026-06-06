from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

# Import your existing classes
from main import Policy, Claim, ClaimService

app = FastAPI()

class ClaimRequest(BaseModel):
    claim_id: str
    policy_id: str
    claim_amount: int
    disease: str
claim_service = ClaimService()

policy = Policy(
    "P001",
    "HealthPlus",
    100000,
    date(2026, 1, 1),
    30
)

policies = {
    "P001": policy
}

@app.get("/")
def home():
    return {
        "message": "PHI Interview Prep"
    }


@app.post("/claim")
def submit_claim(
    claim_request: ClaimRequest
):
    policy = policies.get(
    claim_request.policy_id
)
    if policy is None:
        return {
            "error": "Policy not found"
        }
    print("Policy ID received:", claim_request.policy_id)
    print("Policy found:", policy)

    claim = Claim(
        claim_request.claim_id,
        claim_request.policy_id,
        claim_request.claim_amount,
        claim_request.disease,
        date.today()
    )

    result = claim_service.submit_claim(
        policy,
        claim
    )

    return {
        "result": result,
        "status": claim.status,
        "remaining_coverage": policy.get_remaining_coverage()
    }


@app.get("/policy")
def get_policy():
    return {
            "policy_id": policy.policy_id,
            "policy_name": policy.policy_name,
            "coverage": policy.coverage_amount,
            "remaining_coverage": policy.get_remaining_coverage(),
            "active": policy.active
        }