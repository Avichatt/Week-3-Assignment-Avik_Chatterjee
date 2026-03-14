"""
Day 16 · AM Session · Take-Home Assignment
Part C — Interview Ready
"""

import numpy as np
import scipy.stats as stats

# Q1 — Explain to a product manager: what is the difference between a p-value and a confidence interval? 
# When is each more useful?
"""
Answer:
A p-value tells you IF there is a difference that is unlikely to be due to luck alone. 
It’s like a "yes/no" signal for statistical significance.

A confidence interval tells you the SIZE and RANGE of that difference. 
It gives you a bracket (e.g., "we expect an increase between 2% and 5%").

- A p-value is more useful when you just need to clear a hurdle to prove a theory.
- A confidence interval is more useful when you need to make a business decision based on the magnitude of the effect (e.g., "is the gain worth the cost of development?").
"""

# Q2 (Coding) — Implement ab_test(control, treatment, alpha=0.05)
def ab_test(control, treatment, alpha=0.05):
    # (a) Check normality (Shapiro-Wilk test)
    # If p > 0.05, we assume normality
    _, p_norm_c = stats.shapiro(control)
    _, p_norm_t = stats.shapiro(treatment)
    
    is_normal = (p_norm_c > 0.05) and (p_norm_t > 0.05)
    
    # (b) Select appropriate test
    if is_normal:
        # T-test for normally distributed data
        t_stat, p_value = stats.ttest_ind(treatment, control)
        test_type = "T-test"
    else:
        # Mann-Whitney U for non-normal data
        t_stat, p_value = stats.mannwhitneyu(treatment, control)
        test_type = "Mann-Whitney U"
        
    # Effect Size (Cohen's d)
    mean_diff = np.mean(treatment) - np.mean(control)
    pooled_sd = np.sqrt((np.std(control, ddof=1)**2 + np.std(treatment, ddof=1)**2) / 2)
    effect_size = mean_diff / pooled_sd if pooled_sd != 0 else 0
    
    # 95% CI (Simplified using T-distribution for means)
    se_diff = np.sqrt(np.var(control, ddof=1)/len(control) + np.var(treatment, ddof=1)/len(treatment))
    t_crit = stats.t.ppf(1 - alpha/2, len(control) + len(treatment) - 2)
    ci_95 = (mean_diff - t_crit * se_diff, mean_diff + t_crit * se_diff)
    
    # (c) Return structured dict
    return {
        'test_type': test_type,
        'statistic': t_stat,
        'p_value': p_value,
        'reject_H0': p_value < alpha,
        'effect_size': effect_size,
        'ci_95': ci_95
    }

# Test the function with some example data
control = np.random.normal(10, 2, 50)
treatment = np.random.normal(11, 2, 50)
results = ab_test(control, treatment)
print("--- A/B Test Function Output ---")
for k, v in results.items():
    print(f"{k}: {v}")


# Q3 — You run a test and get p=0.04, but the effect size is 0.02 (very small). 
# Your manager says 'ship it.' What 3 questions would you ask before agreeing?
"""
Answer:
1. "Is this 0.02 effect size practically significant for our business goals?"
   (Does this tiny gain actually impact revenue or user experience in a meaningful way?)

2. "What are the costs associated with shipping and maintaining this change?"
   (If the gain is tiny but the complexity is high, it might not be worth it.)

3. "Could the small effect size be due to a lack of power or a specific segment of users?"
   (Maybe it's working well for some but poorly for others, washing out the main result.)
"""
