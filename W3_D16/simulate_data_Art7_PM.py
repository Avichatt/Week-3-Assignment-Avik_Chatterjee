import pandas as pd
import numpy as np

# Simulate eda_assignment_data.csv for the assignment
np.random.seed(42)
n_rows = 1200

data = {
    'CustomerID': range(1, n_rows + 1),
    'Age': np.random.randint(18, 70, n_rows),
    'AnnualIncome': np.random.normal(60000, 15000, n_rows),
    'SpendingScore': np.random.randint(1, 101, n_rows),
    'ItemsPurchased': np.random.poisson(5, n_rows),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n_rows),
    'Gender': np.random.choice(['Male', 'Female', 'Non-Binary'], n_rows),
    'SatisfactionScore': np.random.randint(1, 6, n_rows),
    'DiscountUsed': np.random.uniform(0, 0.5, n_rows),
    'MembershipDays': np.random.randint(1, 3650, n_rows)
}

df = pd.DataFrame(data)
df.to_csv('C:/Users/Avi/.gemini/antigravity/scratch/Week-3-Assignment-Avik_Chatterjee/W3_D16/eda_assignment_data.csv', index=False)
print("Simulated dataset created.")
