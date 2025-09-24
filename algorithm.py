def calculate_reward(issue, officer):
    if issue.status == "Resolved":
        if issue.verified_by_citizen:
            reward = base_points + (priority_score * 2)
            bonus = max(0, (deadline - resolution_time)) * decay_factor
            officer.points += reward + bonus
        else:
            penalty = penalty_points + (resolution_time - deadline) * penalty_rate
            officer.points -= penalty
    else:
        penalty = penalty_points + (resolution_time - deadline) * penalty_rate
        officer.points -= penalty

def add_preventive_points(officer, activity_type):
    activity_rewards = {
        "maintenance": 15,
        "monthly_report": 20,
        "awareness_drive": 25
    }
    officer.points += activity_rewards.get(activity_type, 0)

def add_participation_bonus(officer, action):
    if action == "weekly_login":
        officer.points += 5
    elif action == "verify_no_issues":
        officer.points += 10

def normalize_score(officer, ward_avg_complaints):
    officer.final_score = (officer.points / (ward_avg_complaints + 1)) * 100
    update_leaderboard(officer.final_score)
