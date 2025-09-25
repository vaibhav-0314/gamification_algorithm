## 📌 Overview

The **Gamification & Leaderboard System** is part of the **Namma Ward Civic Management Platform**.  
It rewards ward officers based on **verified complaint resolution, preventive actions, participation activities, and ward cleanliness**.  

This ensures:  
- Timely complaint resolution  
- Motivation for proactive and preventive actions  
- Fair evaluation for wards with different complaint volumes  
- Transparency through a public leaderboard  

---

## 🎯 Objectives

- Encourage verified and timely complaint resolution  
- Reward preventive & participation activities  
- Provide clean ward bonuses for complaint-free wards  
- Normalize scores across wards to ensure fairness  
- Update leaderboard in real-time for motivation and accountability  

---

## 🛠 Features

- **Verified Complaint Reward** – Points for citizen-verified complaint resolutions  
- **Penalty for Delays / Unverified Resolutions** – Points deducted for late or unverified complaints  
- **Preventive & Participation Points** – Maintenance, awareness drives, weekly login, verify no issues  
- **Clean Ward Bonus** – Extra points if ward has zero complaints in the period  
- **Normalized & Weighted Leaderboard** – Fair ranking across wards of different sizes  
- **Citizen Feedback Influence** – Upvotes increase points, downvotes decrease points  
- **Weekly Leaderboard Update** – Combines reactive & proactive points  

---

## ⚡ Python Functions

### **1. Reward / Penalty Calculation**
```python
def calculate_reward(issue, officer):
    if issue.status == "Resolved":
        if issue.verified_by_citizen:
            reward = base_points + (priority_score * 2)
            bonus = max(0, (deadline - resolution_time)) * decay_factor
            officer.reactive_points += reward + bonus
        else:
            officer.reactive_points -= penalty_points
    else:
        penalty = penalty_points + max(0, (resolution_time - deadline)) * decay_factor
        officer.reactive_points -= penalty


2. Preventive Points:
def add_preventive_points(officer, activity_type):
    activity_rewards = {
        "maintenance": 15,
        "monthly_report": 20,
        "awareness_drive": 25
    }
    officer.proactive_points += activity_rewards.get(activity_type, 0)


3. Participation Bonus:
def add_participation_bonus(officer, action):
    participation_rewards = {
        "weekly_login": 5,
        "verify_no_issues": 10
    }
    officer.proactive_points += participation_rewards.get(action, 0)


4. Complaint-Free Ward Bonus:
def add_complaint_free_bonus(officer, ward):
    if ward.total_complaints_in_period == 0:
        bonus = 20
        officer.proactive_points += bonus
        officer.complaint_free_bonus = bonus


5. Final Score Normalization:
def calculate_final_score(officer, ward_avg_complaints, proactive_weight=0.6, reactive_weight=0.4):
    weighted_score = (proactive_weight * officer.proactive_points) + (reactive_weight * officer.reactive_points)
    officer.final_score = min((weighted_score / (ward_avg_complaints + 1)) * 100, 100)


6. Weekly Leaderboard Update:
def update_weekly_leaderboard(officers):
    for officer in officers:
        officer.weekly_score = officer.final_score + officer.complaint_free_bonus
    leaderboard = sorted(officers, key=lambda x: x.weekly_score, reverse=True)
    return leaderboard


📈 Workflow
Officer resolves a complaint → points calculated based on verification, priority, and timeliness
Preventive & participation activities → extra points added to proactive score
Wards with zero complaints → clean ward bonus applied
Weighted scores calculated → leaderboard updated
Citizen upvotes/downvotes influence reactive points
Weekly leaderboard ensures transparency and officer motivation

🏆 Benefits
Motivates officers to resolve complaints efficiently
Encourages proactive maintenance & awareness drives
Ensures fair evaluation for officers in low-complaint wards
Supports gamified civic management

Provides public transparency through leaderboard

💻 Tech Integration
Backend: Python (Flask / FastAPI)
AI Integration: Prioritizes complaints based on urgency & location
Leaderboard: Updates in real-time after each action
Can be extended to React + Tailwind frontend for live dashboards