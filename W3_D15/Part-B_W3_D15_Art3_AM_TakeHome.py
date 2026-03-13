"""
Part B — Stretch Problem (30%)

Research the Beta distribution. Using scipy.stats.beta: 
(1) plot PDF for Beta(2,5), Beta(5,5), Beta(0.5,0.5); 
(2) explain what each shape means as a prior belief about a coin's bias; 
(3) simulate: if you observe 7 heads in 10 flips, how does the posterior change from a Beta(1,1) prior?
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def run_part_b():
    print("=== Part B: Stretch Problem (Beta Distribution) ===\n")
    
    # 1. Plot PDF for Beta(2,5), Beta(5,5), Beta(0.5,0.5)
    x = np.linspace(0, 1, 500)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, beta.pdf(x, 2, 5), lw=2, label='Beta(2, 5) - Tails biased')
    plt.plot(x, beta.pdf(x, 5, 5), lw=2, label='Beta(5, 5) - Fair biased')
    
    # For Beta(0.5, 0.5), it shoots to infinity at 0 and 1, so we subset x slightly to avoid warnings.
    x_bimodal = np.linspace(0.01, 0.99, 500)
    plt.plot(x_bimodal, beta.pdf(x_bimodal, 0.5, 0.5), lw=2, label='Beta(0.5, 0.5) - Extremely biased')
    
    plt.title('Beta Distribution Prior Shapes (Coin Bias)')
    plt.xlabel('Probability of Heads (θ)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Uncomment to actually exhibit plot window:
    # plt.show()
    print("[Plots Generated - Please uncomment plt.show() to view visually]\n")

    # 2. Explain what each shape means as a prior belief about a coin's bias
    print("2. Prior Explanations:")
    print(" - Beta(2, 5): Represents a strong prior belief that the coin is loaded towards Tails. "
          "The peak (mode) is skewed left (around 0.2), indicating a low probability of observing Heads.")
    print(" - Beta(5, 5): Represents a prior belief that the coin is fair. It forms a symmetric bell-like shape "
          "centered at 0.5. We are moderately confident it's a typical coin since the tails of the distribution drop off.")
    print(" - Beta(0.5, 0.5): A 'bimodal' (U-shaped) prior. It represents a belief that the coin is definitively rigged or highly biased, "
          "but we don't know in which direction. It strongly assumes the coin is either double-headed or double-tailed.")

    # 3. Simulate: if you observe 7 heads in 10 flips, how does the posterior change from a Beta(1,1) prior?
    print("\n3. Simulation of Posterior Update:")
    print("Let the Prior be Beta(1, 1), which is a completely Uniform distribution (we assume any bias is equally likely).")
    print("Observation: 7 Heads (successes) and 3 Tails (failures) in 10 flips.")
    
    # Beta is the conjugate prior to the Binomial distribution.
    # The update rule is incredibly simple: 
    # Posterior alpha = Prior alpha + successes
    # Posterior beta = Prior beta + failures
    
    alpha_prior = 1
    beta_prior = 1
    observed_heads = 7
    observed_tails = 3
    
    alpha_posterior = alpha_prior + observed_heads
    beta_posterior = beta_prior + observed_tails
    
    prior_mean = alpha_prior / (alpha_prior + beta_prior)
    post_mean = alpha_posterior / (alpha_posterior + beta_posterior)
    
    print(f"\nPrior Distribution:     Beta({alpha_prior}, {beta_prior}) -> Mean Expected Bias = {prior_mean:.2f} (50%)")
    print(f"Posterior Distribution: Beta({alpha_posterior}, {beta_posterior}) -> Mean Expected Bias = {post_mean:.2f} (67%)")
    print("\nExplanation:")
    print("By observing 7 Heads, the parameters update strictly additive to Beta(8, 4). "
          "Our belief seamlessly shifted away from uniform uncertainty towards a distinct suspicion "
          "that the coin is biased in favor of Heads (~67% expected probability).")

if __name__ == "__main__":
    run_part_b()
