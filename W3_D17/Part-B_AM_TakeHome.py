"""
Day 17 · AM Session · Take-Home Assignment
Part B: Stretch Problem — NumPy Random Module Deep Dive
"""

import numpy as np
import time

# 1. Compare np.random.default_rng() (new API) vs np.random.seed() (legacy)
print("--- RNG Performance Comparison ---")
n_samples = 1_000_000

# Legacy API
start_legacy = time.time()
np.random.seed(42)
legacy_samples = np.random.normal(0, 1, n_samples)
end_legacy = time.time()
print(f"Legacy (np.random.seed/normal) time: {end_legacy - start_legacy:.4f}s")

# New API
start_new = time.time()
rng = np.random.default_rng(42)
new_samples = rng.normal(0, 1, n_samples)
end_new = time.time()
print(f"New API (default_rng) time: {end_new - start_new:.4f}s")

# 2. Synthetic dataset for linear regression
def generate_regression_data(n=100, seed=42):
    rng = np.random.default_rng(seed)
    
    # X (100 samples, 3 features) from normal distribution
    X = rng.standard_normal((n, 3))
    
    # True weights w
    w = np.array([2.5, -1.3, 0.7])
    
    # Noise from N(0, 0.5)
    noise = rng.normal(0, 0.5, n)
    
    # y = X @ w + noise
    y = X @ w + noise
    
    return X, y, w

X, y, w = generate_regression_data()
print("\n--- Synthetic Regression Data ---")
print(f"X shape: {X.shape}, y shape: {y.shape}")
print(f"First 5 y-values: {y[:5]}")

# 3. Research: What is np.random.Generator and why was it introduced?
"""
Research Answer:
np.random.Generator is the central object for the new random number generation API introduced in NumPy 1.17. 
It was introduced to address several weaknesses of the legacy 'RandomState' (np.random.seed) system, 
including improved performance (especially for complex distributions), better statistical properties 
(using the PCG64 algorithm by default), and better support for parallel computing. 
Unlike the legacy system which relies on a global state, Generator encourages passing 
rng objects explicitly, making code more thread-safe and reproducible across different processes.
"""
