"""
Day 17 · AM Session · Take-Home Assignment
Part C: Interview Ready
"""

import numpy as np

# Q1 (Conceptual): Explain broadcasting rules.
"""
Analogy:
Imagine you are a chef in a restaurant. You have a stack of 10 dinner orders (an array). 
Instead of making each plate one by one, you have a giant 'Stamp' that adds a side of mashed potatoes 
(a single value or a smaller array) to every single plate at once. 
Broadcasting is the rule set that decides if your 'Stamp' is the right size to hit all the plates correctly 
without missing any or overlapping awkwardly.

Formal Rules:
1. If the arrays differ in number of dimensions, the shape of the one with fewer dimensions 
   is padded with ones on its leading (left) side.
2. If the shape of the two arrays does not match in any dimension, the array with a shape 
   equal to 1 in that dimension is stretched to match the other shape.
3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

Example (Works):
A (3x3) and B (1x3) -> B is broadcast across the rows of A.
Example (Fails):
A (3x3) and B (1x2) -> Neither dimension matches and neither is 1.
"""

# Q2 (Coding): Row normalization
def row_normalize(arr: np.ndarray) -> np.ndarray:
    """Normalize each row to sum to 1. Zero-sum rows stay as zeros."""
    row_sums = arr.sum(axis=1, keepdims=True)
    # Using np.where to avoid division by zero
    return np.where(row_sums == 0, 0, arr / row_sums)

# Test Q2
test_arr = np.array([[1, 2, 3], [0, 0, 0], [4, 1, 5]])
print("--- Row Normalization Test ---")
print(row_normalize(test_arr))


# Q3 (Debug): Find and fix the bug
"""
Original Code:
data = np.array([1, 2, 3, 4, 5])
mask = data > 2 and data < 5   # Line A
filtered = data[mask]
result = filtered.reshape(2, 1)

Issues Identified:
1. 'Line A' uses the Python keyword 'and', which is for scalars. For NumPy arrays, we must use 
   the bitwise operator '&' to perform element-wise logical AND.
2. The comparison 'data > 2 and data < 5' will raise a ValueError because an array's truth value is ambiguous.
3. 'result = filtered.reshape(2, 1)' will fail because the filtered array contains only [3, 4] 
   (2 elements), and a (2, 1) reshape is possible, BUT if the mask was slightly different or 
   the data size varied, this hardcoded reshape is risky.

Corrected Version:
"""
data = np.array([1, 2, 3, 4, 5])
mask = (data > 2) & (data < 5)  # Use & and parentheses
filtered = data[mask]
result = filtered.reshape(-1, 1) # Use -1 for flexibility
print("\n--- Debugged Result ---")
print(result)
