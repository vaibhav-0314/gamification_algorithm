## 📌 Overview

The **Gamification Algorithm** is part of the **Namma Ward Civic Management System**.  
It rewards ward officers based on **verified complaint resolution, preventive actions, participation activities, and ward cleanliness**.  

This ensures:  
- Timely complaint resolution  
- Motivation for proactive actions  
- Fair evaluation for all wards  
- Transparency through a public leaderboard  

---

## 🎯 Objectives

- Encourage verified and timely complaint resolution  
- Reward preventive & participation activities  
- Provide clean ward bonuses  
- Normalize scores across wards  
- Update leaderboard in real-time  

---

## 🛠 Features

- **Verified Complaint Reward** – Points for citizen-verified resolutions  
- **Penalty for Delays / Unverified Resolutions** – Points deducted for late or unverified complaints  
- **Preventive & Participation Points** – Maintenance, awareness drives, weekly login, verify no issues  
- **Clean Ward Bonus** – Extra points if ward has zero complaints  
- **Normalized Leaderboard** – Fair ranking across wards of different sizes  

---

## ⚡ Python Functions

### **1. Reward / Penalty Calculation**
```python
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


2. Preventive Points
def add_preventive_points(officer, activity_type):
    activity_rewards = {
        "maintenance": 15,
        "monthly_report": 20,
        "awareness_drive": 25
    }
    officer.points += activity_rewards.get(activity_type, 0)


3. Participation Bonus
def add_participation_bonus(officer, action):
    if action == "weekly_login":
        officer.points += 5
    elif action == "verify_no_issues":
        officer.points += 10


4. Normalize Score
def normalize_score(officer, ward_avg_complaints):
    officer.final_score = (officer.points / (ward_avg_complaints + 1)) * 100
    update_leaderboard(officer.final_score)


📈 Workflow:
1.Officer resolves a complaint → points calculated based on verification & timeliness
2.Preventive & participation activities → extra points added
3.Wards with zero complaints → clean ward bonus applied
4.Scores normalized → leaderboard updated
5.Public leaderboard ensures transparency and motivation


🏆 Benefits:
1.Motivates officers to resolve complaints efficiently
2.Encourages proactive maintenance & awareness
3.Ensures fair evaluation for officers in low-complaint wards
4.Supports gamified civic management


💻 Tech Integration:
1.Backend: Python (Flask or similar)
2.Integrated with AI-prioritized complaint handling
3.Leaderboard updates in real-time after each action