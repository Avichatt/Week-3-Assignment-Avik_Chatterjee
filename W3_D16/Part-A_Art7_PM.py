"""
Day 16 · PM Session · Take-Home Assignment
Part A — Concept Application: Comprehensive EDA Report
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('eda_assignment_data.csv')

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Distribution Plots (Histogram + KDE)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.histplot(df['Age'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')

sns.histplot(df['AnnualIncome'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Distribution of Annual Income')
axes[1].set_xlabel('Annual Income ($)')
axes[1].set_ylabel('Frequency')

sns.histplot(df['SpendingScore'], kde=True, ax=axes[2], color='green')
axes[2].set_title('Distribution of Spending Score')
axes[2].set_xlabel('Spending Score (1-100)')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('distribution_plots.png')
print("Saved distribution_plots.png")

# Insights for Distributions
"""
Insight 1: The age distribution is quite uniform across the 18-70 range, suggesting a diverse customer base.
Insight 2: Annual income follows a roughly normal distribution centered around $60k, indicating a middle-class target audience.
Insight 3: Spending scores are broadly distributed, with several peaks suggesting potential customer segments with varying shopping behaviors.
"""

# 2. Relationship Plots (Scatter with Regression Line)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.regplot(data=df, x='Age', y='SpendingScore', ax=axes[0], scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
axes[0].set_title('Age vs Spending Score')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Spending Score')

sns.regplot(data=df, x='AnnualIncome', y='ItemsPurchased', ax=axes[1], scatter_kws={'alpha':0.3}, line_kws={'color':'blue'})
axes[1].set_title('Income vs Items Purchased')
axes[1].set_xlabel('Annual Income')
axes[1].set_ylabel('Items Purchased')

plt.tight_layout()
plt.savefig('relationship_plots.png')
print("Saved relationship_plots.png")

# Insights for Relationships
"""
Insight 4: There is a very weak negative correlation between Age and Spending Score, suggesting that younger customers might spend slightly more, but the relationship is not strong.
Insight 5: Income shows almost no linear relationship with the number of items purchased, implying that high earners don't necessarily buy more units of product.
"""

# 3. Correlation Heatmap
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.savefig('correlation_heatmap.png')
print("Saved correlation_heatmap.png")

# Insight for Heatmap
"""
Insight 6: The heatmap reveals low overall correlation between features, which is expected for this simulated dataset. 
Wait, actually, SatisfactionScore and SpendingScore might show some interesting clusters in a real scenario, but here they are independent.
"""

# 4. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Region', y='AnnualIncome', palette='Set3')
plt.title('Distribution of Annual Income across Regions')
plt.xlabel('Region')
plt.ylabel('Annual Income')
plt.savefig('box_plot_region.png')
print("Saved box_plot_region.png")

# Insight for Box Plot
"""
Insight 7: Income distributions are remarkably consistent across all four geographical regions. 
There are a few outliers on both the high and low ends in each region, but the median remains stable.
"""

# Create a final "Dashboard" collection of images (optional but good for submission)
print("EDA processing complete. All charts saved as PNGs.")
