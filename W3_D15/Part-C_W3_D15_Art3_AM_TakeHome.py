"""
Part C — Interview Ready (20%)

Q1 — Explain the base rate fallacy using a medical test example. 
Why does a 99% accurate test for a 1-in-10,000 disease still give mostly false positives?

Q2 (Coding) — Write simulate_clt(distribution, params, n_samples, n_simulations) that simulates the CLT 
for any scipy.stats distribution. It should generate sample means, plot the histogram, overlay the theoretical normal approximation.

Q3 — Customer purchase amounts follow an exponential distribution. 
Why is mean purchase amount a misleading metric for investors? What would you show instead?
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def answer_q1():
    print("=== Q1: Base Rate Fallacy ===")
    explanation = (
        "The base rate fallacy occurs when people accurately assess the conditional probability of an event "
        "but completely ignore the overall likelihood (base rate) of that event occurring in the population.\n"
        "\nLet's map out the 1-in-10,000 disease with a 99% accurate test:\n"
        " - Imagine a population of exactly 10,000 people.\n"
        " - True Positive scenario: Because the base rate is 1/10,000, exactly 1 person has the disease. "
        "The 99% accurate test spots this and correctly reports positive (1 True Positive).\n"
        " - False Positive scenario: 9,999 people are completely healthy. "
        "The test has a 1% error rate for predicting healthy people, meaning 1% of 9,999 = ~100 False Positives.\n"
        "\nIf you test positive, you are 1 of the 101 people (1 true + 100 false) who got a positive result.\n"
        "Probability you actually have the disease given a positive result: 1 / 101 = ~0.99%.\n"
        "Conclusion: Even with 99% accuracy, the test yields mostly false positives because the true incidence "
        "of the disease is exceptionally lower than the error rate of the test itself."
    )
    print(explanation)

def simulate_clt(distribution, params, n_samples=30, n_simulations=1000):
    """
    Simulates the CLT for any scipy.stats distribution.
    Generates sample means, plots the histogram, overlays the theoretical normal approximation.
    """
    # 1. Generate sample means
    sample_means = []
    for _ in range(n_simulations):
        # Generate 'n_samples' random variates based on distribution and its parameters
        sample = distribution.rvs(**params, size=n_samples)
        sample_means.append(np.mean(sample))
        
    sample_means = np.array(sample_means)
    
    # 2. Compute theoretical Normal parameters using Population Mean and Std Dev
    pop_mean = distribution.mean(**params)
    pop_std = distribution.std(**params)
    
    # The Standard Error (SE) acts as standard deviation of the sample means
    se = pop_std / np.sqrt(n_samples)
    
    # 3. Plotting
    plt.figure(figsize=(9, 6))
    
    # Histogram of simulated means (normalized with density=True)
    count, bins, ignored = plt.hist(sample_means, bins=40, density=True, alpha=0.6, 
                                    color='salmon', edgecolor='black', label='Simulated Sample Means')
    
    # Normal approximation overlay
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 200)
    pdf_normal = stats.norm.pdf(x, loc=pop_mean, scale=se)
    
    plt.plot(x, pdf_normal, 'k', linewidth=2.5, 
             label=f'Theoretical Normal\n$\mu$={pop_mean:.2f}, $SE$={se:.2f}')
    
    plt.title(f'Central Limit Theorem Simulation\n(n_samples={n_samples}, n_simulations={n_simulations})')
    plt.xlabel('Sample Mean')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Uncomment to actually launch the plot window:
    # plt.show()
    print(f"\n[Plot Generated for CLT Simulation: {distribution.name} distribution.]\n")


def answer_q3():
    print("=== Q3: Exponential Purchase Mislead ===")
    explanation = (
        "The exponential distribution is highly skewed to the right (a long right tail). "
        "This means the vast bulk of transaction sizes are extremely small (e.g., occasional small purchases), "
        "but there are a handful of exceedingly large, 'whale' transactions.\n\n"
        "Why is mean misleading?\n"
        "Because the arithmetic mean averages everything out, those sparse massive transactions will 'pull' "
        "the mean significantly upward. Investors might see an average purchase volume of $250 and believe "
        "a typical customer spends that much, failing to realize 80% of customers probably spend only $20.\n\n"
        "What to show instead:\n"
        "To provide a realistic portrait to investors, use the Median (the 50th percentile) as the primary metric, "
        "since it represents the exact midpoint of user behavior and is robust to extreme outliers.\n"
        "Additionally, showing the Interquartile Range (IQR) or the 90th percentile alongside the median "
        "clearly uncovers the distinct behavior between common shoppers and the high-yield minority."
    )
    print(explanation)

if __name__ == "__main__":
    answer_q1()
    
    print("\n--- Running CLT simulation for Exponential (lambda=0.5 / scale=2.0) ---")
    simulate_clt(stats.expon, {'scale': 2.0}, n_samples=50, n_simulations=1500)
    
    answer_q3()
