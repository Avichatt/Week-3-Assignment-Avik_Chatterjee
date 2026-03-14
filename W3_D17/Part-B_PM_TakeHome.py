"""
Day 17 · PM Session · Take-Home Assignment
Part B: Stretch Problem — NumPy Linear Algebra (np.linalg)
"""

import numpy as np

# 1. Matrix operations
A = np.array([[4, 7, 2],
              [3, 5, 1],
              [2, 6, 8]])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
eigenvalues, eigenvectors = np.linalg.eig(A)

print("--- Matrix Properties ---")
print(f"Determinant: {det_A:.4f}")
print(f"Inverse of A:\n{inv_A}")

# Verify A @ A_inv = Identity
I = np.eye(3)
is_identity = np.allclose(A @ inv_A, I)
print(f"Is A @ A_inv approximately Identity? {is_identity}")

# 2. Solve a system of linear equations
# 2x + 3y = 8
# 4x + y = 10
# Ax = b
coeff_matrix = np.array([[2, 3], [4, 1]])
const_vector = np.array([8, 10])
solution = np.linalg.solve(coeff_matrix, const_vector)
print(f"\n--- System Solution ---")
print(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}")

# 3. Research: What is np.linalg.svd() and where is it used in ML?
"""
Research Answer:
np.linalg.svd() stands for Singular Value Decomposition. It factorizes a matrix into 
three constituent matrices: U (left singular vectors), S (singular values), and Vh (right singular vectors). 
In Machine Learning, SVD is foundational for:
1. Dimensionality Reduction: It is the math behind Principal Component Analysis (PCA).
2. Recommendation Systems: Used in Collaborative Filtering to discover latent features 
   (e.g., Netflix predicting movie ratings).
3. Latent Semantic Analysis (LSA): Used in NLP to find relationships between terms and documents.
"""
