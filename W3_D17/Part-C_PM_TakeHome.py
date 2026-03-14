"""
Day 17 · PM Session · Take-Home Assignment
Part C: Interview Ready
"""

import numpy as np

# Q1 (Conceptual): Vectorization vs Loops
"""
Performance Problem: 
The code uses nested Python loops. Python is an interpreted language, so each iteration 
involves high overhead (checking types, dispatching operations). For a 1000x1000 matrix, 
this loop executes 1,000,000 times in pure Python.

Vectorized Rewrite:
result = data**2 + 2*data + 1

Estimate Table:
For a 1000x1000 matrix (1M elements), the speedup factor is typically 50x to 100x. 
NumPy executes the operation in compiled C/C++ or Fortran, utilizing CPU-level optimizations 
like SIMD (Single Instruction, Multiple Data).
"""

# Q2 (Coding): K-Nearest Neighbors using only NumPy
def k_nearest(data: np.ndarray, point: np.ndarray, k: int) -> np.ndarray:
    """Return indices of k closest points to 'point' in 'data'."""
    # Distance: sqrt(sum((data - point)^2))
    # We can omit sqrt for comparison purposes to save computation
    distances = np.sum((data - point)**2, axis=1)
    return np.argsort(distances)[:k]

# Test Q2
test_data = np.random.rand(10, 2)
test_point = np.array([0.5, 0.5])
print("--- K-Nearest Neighbors ---")
print(f"Top 3 indices: {k_nearest(test_data, test_point, 3)}")


# Q3 (Debug): Normalization bugs
"""
Original Code:
means = data.mean(axis=1)     # Line A
stds = data.std(axis=1)       # Line B
normalized = (data - means) / stds  # Line C

Bugs Identified:
1. Axis choice: To normalize columns, axis should be 0, not 1. axis=1 averages across rows.
2. Broadcasting Shape: means/stds will be (100,) arrays. Subtracting them from a (100, 5) 
   array will fail or broadcast incorrectly unless reshaped or keepdims=True is used.
3. Lack of keepdims: Without keepdims=True, the results are flattened, preventing 
   correct broadcasting during the subtraction/division phase.

Corrected Version:
"""
data = np.random.randn(100, 5)
col_means = data.mean(axis=0, keepdims=True)
col_stds = data.std(axis=0, keepdims=True)
normalized = (data - col_means) / col_stds
print("\n--- Corrected Normalization ---")
print(f"Mean of first col after: {normalized[:, 0].mean():.4f} (expected ~0)")
print(f"Std of first col after: {normalized[:, 0].std():.4f} (expected ~1)")
