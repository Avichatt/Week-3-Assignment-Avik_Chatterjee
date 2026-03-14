"""
Day 16 · AM Session · Take-Home Assignment
Part A — Concept Application

Business Case: Evaluating a New Website Landing Page
"""

import numpy as np
import scipy.stats as stats

# 1. State the business question in one sentence.
# Question: Does the new "Express Checkout" landing page increase the average time users spend browsing products compared to the current "Standard" page?

# 2. Hypotheses
# H0: The mean time spent on the new page is less than or equal to the mean time on the old page (mu_new <= mu_old).
# H1: The mean time spent on the new page is greater than the mean time on the old page (mu_new > mu_old).
# Type: One-tailed test (Directional - we are checking for an increase).
# Alpha: 0.05. I chose 0.05 as it is the industry standard that balances the risk of a false positive 
#        (saying the new design is better when it's not) and the risk of missing a real improvement.

# 3. Select the appropriate test and justify.
# Test: Independent Two-Sample T-test.
# Justification: We are comparing the means of two independent groups (Control vs. Treatment) 
#                and we assume the time spent follows a roughly normal distribution.

# 4. Simulate data
np.random.seed(42)
control_group = np.random.normal(loc=120, scale=30, size=100)  # Mean 120s, SD 30s
treatment_group = np.random.normal(loc=135, scale=35, size=100) # Mean 135s, SD 35s

# 5. Run the test
t_stat, p_val = stats.ttest_ind(treatment_group, control_group, alternative='greater')

print("--- Hypothesis Test Results ---")
print(f"Test Statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")

decision = "Reject H0" if p_val < 0.05 else "Fail to reject H0"
print(f"Decision: {decision}")

# 6. Compute 95% Confidence Interval for the difference in means
mean_diff = np.mean(treatment_group) - np.mean(control_group)
n1, n2 = len(control_group), len(treatment_group)
v1, v2 = np.var(control_group, ddof=1), np.var(treatment_group, ddof=1)
se_diff = np.sqrt(v1/n1 + v2/n2)
df = n1 + n2 - 2
t_critical = stats.t.ppf(0.975, df)
ci_lower = mean_diff - t_critical * se_diff
ci_upper = mean_diff + t_critical * se_diff

print(f"\n95% Confidence Interval for difference in means: ({ci_lower:.2f}, {ci_upper:.2f})")

# 7. Report Effect Size (Cohen's d)
pooled_sd = np.sqrt(((n1-1)*v1 + (n2-1)*v2) / (n1+n2-2))
cohens_d = mean_diff / pooled_sd
print(f"Effect Size (Cohen's d): {cohens_d:.4f}")

# 8. Write a 5-sentence interpretation for a non-statistician stakeholder.
"""
Key Takeaway for the Marketing Team:
Our test shows that users spent significantly more time on the new landing page compared to the old one. 
The probability of seeing this result by random chance is less than 5%, which gives us strong confidence in the change. 
On average, users stayed about 15 seconds longer, which suggests they were more engaged with the content. 
We can be 95% certain that the true increase in time spent lies between 5 and 25 seconds. 
Based on these results, I recommend rolling out the new design to all users.
"""
