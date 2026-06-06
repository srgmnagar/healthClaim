from datetime import date, datetime

class Policy:
    def __init__(
            self,
            policy_id,
            policy_name,
            coverage_amount,
            start_date,
            waiting_period_days,
            active=True
    ):
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.coverage_amount = coverage_amount
        self.start_date = start_date
        self.waiting_period_days = waiting_period_days
        self.active = active
        self.claims=[]
    def isActive(self):
         return self.active
    def has_completed_waiting_period(self,current_date):

        days_passed = (
        current_date - self.start_date
        ).days
        return (
                days_passed
                >=
                self.waiting_period_days
        )
    def get_remaining_coverage(self):
        for claim in self.claims:
            if claim.status=="APPROVED":
                total_claimed = claim.claim_amount
        return self.coverage_amount - total_claimed
    def can_cover(self, amount):
        return (
                self.get_remaining_coverage()
                >= amount
        )

class Claim:
    def __init__(
        self,
        claim_id,
        policy_id,
        claim_amount,
        disease,
        claim_date
    ):
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.claim_amount = claim_amount
        self.disease = disease
        self.claim_date = claim_date

        self.status = "PENDING"

class User:
    def __init__(
        self,
        user_id,
        name,
        email
    ):
        self.user_id = user_id
        self.name = name
        self.email = email

        self.policies = []


rahul = User(
    "U001",
    "Rahul",
    "rahul@gmail.com"
)
policy = Policy(
    "P001",
    "HealthPlus",
    100000,
    date(2026,1,1),
    30
)
claim = Claim(
    "C001",
    "P001",
    50000,
    "Diabetes",
    date(2026,2,15)
)
rahul.policies.append(policy)

policy.claims.append(claim)
print(rahul.name)
print(policy.policy_id)
print(claim.claim_amount)
for policy in rahul.policies:
    print(policy.policy_id)
    print(policy.coverage_amount)
for claim in policy.claims:
        print(claim.claim_id)
        print(claim.claim_amount)

print(policy.has_completed_waiting_period(date(2026,2,15)))

claim.status = "APPROVED"

policy.claims.append(claim)
print(
    policy.get_remaining_coverage()
)
print(policy.can_cover(60000))