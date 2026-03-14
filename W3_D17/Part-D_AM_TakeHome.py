"""
Day 17 · AM Session · Take-Home Assignment
Part D: AI-Augmented Task
"""

# 1. Exact Prompt:
# "Write a NumPy function that performs min-max normalization on a 2D array, scaling each column to [0, 1] range."

# 2. AI's Output:
"""
import numpy as np

def min_max_normalize(arr):
    col_min = arr.min(axis=0)
    col_max = arr.max(axis=0)
    return (arr - col_min) / (col_max - col_min)
"""

# 3. Critical Evaluation:
"""
Evaluation:
The AI provided a concise and truly vectorized solution. It correctly identifies the axes 
needed for column-wise operations and leverages NumPy broadcasting to subtract mins 
and divide by ranges without any explicit loops. 

However, it fails significantly on a common edge case: constant columns. If a column has all identical 
values (e.g., all 5.0), the denominator (col_max - col_min) becomes zero, resulting in a 
RuntimeWarning and an array filled with NaNs or infs for that column. 

To make this portfolio-quality, I would implement a check for the range. Using np.where to 
ensure we only divide by non-zero ranges, or adding a small epsilon, would make the function 
robust. Additionally, adding 'keepdims=True' in the min/max calculations would make the 
broadcasting more explicit and less prone to errors if the input shape varies.
"""

# Implementation of the improved version for verification
import numpy as np

def robust_min_max_normalize(arr):
    col_min = arr.min(axis=0, keepdims=True)
    col_max = arr.max(axis=0, keepdims=True)
    col_range = col_max - col_min
    # Handle division by zero
    return np.where(col_range == 0, 0, (arr - col_min) / col_range)

# Test
test_data = np.array([[10, 5], [20, 5], [30, 5]])
print("--- Robust Min-Max Normalization (Handles constant column) ---")
print(robust_min_max_normalize(test_data))
