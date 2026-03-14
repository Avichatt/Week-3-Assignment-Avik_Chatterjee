"""
Day 16 · AM Session · Take-Home Assignment
Part B — Stretch Problem: Multiple Comparison Problem (p-hacking)
"""

import numpy as np

# Research: What is the Multiple Comparison Problem?
# The multiple comparison problem occurs when one considers a set of statistical inferences simultaneously.
# If we run 20 independent tests, each with a 5% chance of a false positive (Type I error), 
# the overall probability of getting AT LEAST one false positive increases dramatically.

# Calculation:
alpha = 0.05
n_tests = 20
prob_no_false_positive = (1 - alpha) ** n_tests
prob_at_least_one_false_positive = 1 - prob_no_false_positive

print(f"Theoretical probability of at least one false positive in {n_tests} tests: {prob_at_least_one_false_positive:.4f}")

# Simulation to verify
def simulate_multiple_tests(n_sims=10000, n_tests=20, alpha=0.05):
    false_positive_incidents = 0
    for _ in range(n_sims):
        # Generate 20 random p-values (assuming H0 is true, p-values are uniformly distributed)
        p_values = np.random.uniform(0, 1, n_tests)
        # Check if any p-value is less than alpha
        if np.any(p_values < alpha):
            false_positive_incidents += 1
    return false_positive_incidents / n_sims

sim_result = simulate_multiple_tests()
print(f"Simulated probability of at least one false positive: {sim_result:.4f}")

# Implementing Bonferroni Correction
bonferroni_alpha = alpha / n_tests
print(f"\nOriginal Alpha: {alpha}")
print(f"Corrected Bonferroni Alpha: {bonferroni_alpha}")

# Re-running simulation with Bonferroni Correction
corrected_sim_result = simulate_multiple_tests(alpha=bonferroni_alpha)
print(f"Simulated probability with Bonferroni correction: {corrected_sim_result:.4f}")

# Comparison:
# The original alpha (0.05) led to a ~64% chance of at least one false positive.
# The Bonferroni correction brought this overall error rate back down to approximately 0.05, 
# making the testing process much more conservative and reliable.
