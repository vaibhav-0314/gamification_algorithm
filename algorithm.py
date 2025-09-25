# ---------------- Namma Ward Leaderboard & Gamification ----------------

class Officer:
    def __init__(self, name, ward):
        self.name = name
        self.ward = ward
        self.reactive_points = 0  # points from complaint-solving
        self.proactive_points = 0 # points from preventive/clean ward actions
        self.final_score = 0
        self.complaint_free_bonus = 0

class Ward:
    def __init__(self, name, total_complaints):
        self.name = name
        self.total_complaints_in_period = total_complaints
        self.ward_avg_complaints = total_complaints

# ---------------- Points Calculation ----------------

def calculate_reward(issue, officer, base_points=10, penalty_points=5, decay_factor=0.5):
    """
    Calculate reactive points for a single complaint.
    """
    status = issue['status']
    verified = issue.get('verified_by_citizen', False)
    priority_score = issue.get('priority_score', 1)
    resolution_time = issue.get('resolution_time', 1)
    deadline = issue.get('deadline', 1)

    if status == "Resolved":
        if verified:
            reward = base_points + (priority_score * 2)
            bonus = max(0, (deadline - resolution_time)) * decay_factor
            officer.reactive_points += reward + bonus
        else:
            officer.reactive_points -= penalty_points
    else:
        penalty = penalty_points + max(0, (resolution_time - deadline)) * decay_factor
        officer.reactive_points -= penalty

def add_preventive_points(officer, activity_type):
    activity_rewards = {
        "maintenance": 15,
        "monthly_report": 20,
        "awareness_drive": 25
    }
    officer.proactive_points += activity_rewards.get(activity_type, 0)

def add_participation_bonus(officer, action):
    participation_rewards = {
        "weekly_login": 5,
        "verify_no_issues": 10
    }
    officer.proactive_points += participation_rewards.get(action, 0)

def add_complaint_free_bonus(officer, ward):
    if ward.total_complaints_in_period == 0:
        bonus = 20
        officer.proactive_points += bonus
        officer.complaint_free_bonus = bonus
    else:
        officer.complaint_free_bonus = 0

def calculate_final_score(officer, ward_avg_complaints, proactive_weight=0.6, reactive_weight=0.4):
    """
    Weighted score prioritizing clean wards.
    """
    weighted_score = (proactive_weight * officer.proactive_points) + (reactive_weight * officer.reactive_points)
    officer.final_score = min((weighted_score / (ward_avg_complaints + 1)) * 100, 100)

# ---------------- Simulation ----------------

# Create wards
ward_A = Ward("Ward A", total_complaints=50)
ward_B = Ward("Ward B", total_complaints=0)

# Create officers
officer1 = Officer("Alice", ward_A)
officer2 = Officer("Bob", ward_B)

# Sample complaints for Ward A
complaints_A = [
    {"status": "Resolved", "verified_by_citizen": True, "priority_score": 2, "resolution_time": 1, "deadline": 2} for _ in range(50)
]

# Calculate reactive points
for issue in complaints_A:
    calculate_reward(issue, officer1)

# Add proactive points
add_preventive_points(officer1, "maintenance")
add_participation_bonus(officer1, "weekly_login")

# Ward B officer: complaint-free bonus + preventive/participation
add_complaint_free_bonus(officer2, ward_B)
add_participation_bonus(officer2, "verify_no_issues")

# Normalize final scores
calculate_final_score(officer1, ward_A.ward_avg_complaints)
calculate_final_score(officer2, ward_B.ward_avg_complaints)

# ---------------- Leaderboard ----------------

officers = [officer1, officer2]
leaderboard = sorted(officers, key=lambda x: x.final_score, reverse=True)

print("---- Leaderboard ----")
for idx, officer in enumerate(leaderboard, 1):
    print(f"{idx}. {officer.name} (Ward {officer.ward.name}) | Final Score: {officer.final_score} | "
          f"Reactive: {officer.reactive_points} | Proactive: {officer.proactive_points}")
