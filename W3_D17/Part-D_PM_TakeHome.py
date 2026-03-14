"""
Day 17 · PM Session · Take-Home Assignment
Part D: AI-Augmented Task — IQR Outlier Detection
"""

import numpy as np

# 1. Exact Prompt:
# "Write a NumPy function that performs IQR-based outlier detection on each column of a 2D array, replacing outliers with the column median."

# 2. AI's Output:
"""
import numpy as np

def handle_outliers_iqr(df_array):
    Q1 = np.percentile(df_array, 25, axis=0)
    Q3 = np.percentile(df_array, 75, axis=0)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    medians = np.median(df_array, axis=0)
    
    # Replace outliers with column medians
    for i in range(df_array.shape[1]):
        outliers = (df_array[:, i] < lower_bound[i]) | (df_array[:, i] > upper_bound[i])
        df_array[outliers, i] = medians[i]
    
    return df_array
"""

# 3. Critical Evaluation:
"""
Evaluation:
The AI correctly implements the IQR logic (Q3-Q1) and identifies the correct axis (axis=0) 
for column-wise operations. It also correctly calculates the bounds.

Major Critique:
- Hidden Loop: The implementation uses a for-loop to iterate over columns. This is 
  inefficient for high-dimensional data. A truly vectorized approach would use 
  broadcasting with boolean masking across the entire 2D array at once.
- Side Effect: The function modifies the input array in-place (df_array[...]=...), which 
  can lead to bugs if the user expected to keep the original data. A .copy() should be used.
- Robustness: It doesn't handle cases where IQR might be 0, though that's less critical 
  for outlier detection than for scaling.

Portfolio Improvement:
I would rewrite this using np.where() and direct 2D broadcasting to remove the loop 
and ensure no side effects on the original array.
"""

# Implementation of the improved vectorized version
def robust_iqr_cleaner(arr):
    data = arr.copy()
    q1 = np.percentile(data, 25, axis=0, keepdims=True)
    q3 = np.percentile(data, 75, axis=0, keepdims=True)
    iqr = q3 - q1
    
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    medians = np.median(data, axis=0, keepdims=True)
    
    # Broadcast comparison across all rows/cols
    outlier_mask = (data < lower) | (data > upper)
    # Broadcast medians based on the mask
    return np.where(outlier_mask, medians, data)

# Test on data with a known outlier
test_data = np.array([[10, 5], [12, 6], [11, 5], [1000, 5]]) # 1000 is outlier
cleaned = robust_iqr_cleaner(test_data)
print("--- IQR Vectorized Cleaning Result ---")
print(f"Original:\n{test_data}")
print(f"Cleaned:\n{cleaned}")
