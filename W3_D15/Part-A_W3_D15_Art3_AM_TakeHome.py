"""
Part A — Concept Application (40%)

For each of 5 real-world scenarios: 
(a) identify distribution, 
(b) justify with 2 specific reasons, 
(c) sketch the PDF/PMF by hand, 
(d) compute probability using scipy.stats.
"""

from scipy.stats import poisson, binom, norm

def compute_probabilities():
    print("=== Part A: Concept Application ===")
    
    # 1. Website traffic: 200 requests/minute on average. P(more than 220 requests in a minute)?
    # (a) Distribution: Poisson Distribution
    # (b) Justification:
    #     1. It models the count of discrete events (website requests) occurring in a fixed interval of time (one minute).
    #     2. The events happen independently of each other at a known constant average rate (lambda = 200 req/min).
    # (c) Sketch hand-drawn instructions: Draw a slightly right-skewed but nearly symmetric bell shape for a discrete PMF, peaking at x = 200.
    prob_1 = poisson.sf(220, mu=200) # sf is 1 - cdf, which is exactly P(X > 220)
    print(f"\n1. Website traffic (Poisson, mu=200)")
    print(f"   P(>220 requests) = {prob_1:.4f}")

    # 2. Quality control: 2% defective bolts. In a batch of 50, P(exactly 3 defective)?
    # (a) Distribution: Binomial Distribution
    # (b) Justification:
    #     1. There is a fixed number of independent trials (n = 50 bolts).
    #     2. Each trial has exactly two outcomes (defective or not) with a constant probability of success (p = 0.02).
    # (c) Sketch hand-drawn instructions: Draw a highly right-skewed discrete PMF, peaking around x = 1 (since mean = np = 1).
    prob_2 = binom.pmf(3, n=50, p=0.02)
    print(f"\n2. Quality control (Binomial, n=50, p=0.02)")
    print(f"   P(exactly 3 defective) = {prob_2:.4f}")

    # 3. Delivery times: N(45 min, 8^2). P(delivery > 60 min)? P(between 40 and 50 min)?
    # (a) Distribution: Normal Distribution
    # (b) Justification:
    #     1. Specifically stated as N(45, 8^2).
    #     2. Delivery time represents a physical continuous measurement, often resulting from the sum of many independent small factors (traffic, route, weather) leading to a symmetric bell curve shape.
    # (c) Sketch hand-drawn instructions: Draw a symmetric continuous bell curve centered precisely at mean = 45, showing standard deviations at 37 and 53 (width of 8).
    prob_3_a = norm.sf(60, loc=45, scale=8)
    prob_3_b = norm.cdf(50, loc=45, scale=8) - norm.cdf(40, loc=45, scale=8)
    print(f"\n3. Delivery times (Normal, mu=45, sigma=8)")
    print(f"   P(delivery > 60) = {prob_3_a:.4f}")
    print(f"   P(40 < delivery < 50) = {prob_3_b:.4f}")

    # 4. Customer arrivals: 10/hour. P(no customers in next 6 minutes)?
    # (a) Distribution: Poisson Distribution
    # (b) Justification:
    #     1. Models the discrete count of events (arrivals) over a continuous specific time interval (6 minutes).
    #     2. The arrivals are assumed to be independent random events occurring at a constant overall rate.
    # Note: Rate for 6 minutes exactly = 10 * (6 / 60) = 1 customer per 6 minutes.
    # (c) Sketch hand-drawn instructions: Draw a discrete PMF that decays rapidly starting from its peak at either x=0 or x=1, representing lambda=1.
    prob_4 = poisson.pmf(0, mu=1)
    print(f"\n4. Customer arrivals (Poisson, lambda=1 per 6 min)")
    print(f"   P(no customers in 6 min) = {prob_4:.4f}")

    # 5. Class of 35 students. Using CLT, approximate the distribution of the class average score.
    # (a) Distribution: Normal Distribution
    # (b) Justification:
    #     1. The Central Limit Theorem (CLT) states that the distribution of sample means approaches normality, regardless of the population distribution.
    #     2. As long as the sample size is sufficiently large, which n = 35 is (it satisfies the >= 30 rule of thumb).
    # (c) Sketch hand-drawn instructions: Draw a continuous normal bell curve centered at the estimated population mean with a comparatively narrow spread (sigma/sqrt(n)).
    print(f"\n5. Class average score")
    print(f"   Approximated Distribution: Normal Distribution (due to CLT, n=35 >= 30).")

if __name__ == "__main__":
    compute_probabilities()
