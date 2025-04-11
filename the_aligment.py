import numpy as np

male_applicants = np.random.binomial(1, 0.8, 1000)  # higher historical hiring rate
female_applicants = np.random.binomial(1, 0.4, 1000)  # lower historical hiring rate

print(f"Male hiring rate: {male_applicants.mean():.2f}")
print(f"Female hiring rate: {female_applicants.mean():.2f}")

# Opaque model example (black box):
def black_box_model(x):
    return np.random.choice(['Hire', 'Reject'], p=[0.8, 0.2])

# Transparent model example (interpretable rules):
def interpretable_model(experience_years, education_level):
    if experience_years >= 5 and education_level >= 3:
        return 'Hire'
    else:
        return 'Reject'

print("Opaque model decision:", black_box_model(None))
print("Interpretable model decision:", interpretable_model(6, 4))


reward = 0
actions = ['race properly to win', 'exploit unintended reward by hitting targets repeatedly']

chosen_action = actions[1]
reward += 1000 if chosen_action == actions[1] else 100

print(f"AI agent chooses to '{chosen_action}' achieving reward: {reward}")