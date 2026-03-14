"""
Day 16 · PM Session · Take-Home Assignment
Part D — AI-Augmented Task: AI Script Evaluation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. AI Output Generation (Mocked AI Script for Retail Sales)
"""
Prompt: 'Generate a complete Python EDA script for a retail sales dataset. 
Include 6 charts: distributions, correlations, time trends, category comparisons, and one unusual/creative chart.'
"""

# START OF AI GENERATED SCRIPT
def run_ai_eda():
    # Simulate retail data
    np.random.seed(1)
    dates = pd.date_range(start='2023-01-01', periods=1000, freq='D')
    categories = ['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports']
    ai_df = pd.DataFrame({
        'Date': np.random.choice(dates, 1000),
        'Sales': np.random.uniform(10, 500, 1000),
        'Category': np.random.choice(categories, 1000),
        'Profit': np.random.uniform(-50, 200, 1000),
        'Customer_Rating': np.random.randint(1, 6, 1000)
    })
    ai_df = ai_df.sort_values('Date')

    # Chart 1: Distribution (Sales)
    plt.figure(figsize=(8, 4))
    sns.histplot(ai_df['Sales'], color='purple', kde=True)
    plt.title('AI: Sales Distribution')
    plt.savefig('ai_sales_dist.png')

    # Chart 2: Correlation (Heatmap)
    plt.figure(figsize=(8, 6))
    sns.heatmap(ai_df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='RdYlGn')
    plt.title('AI: Correlation Map')
    plt.savefig('ai_corr.png')

    # Chart 3: Time Trend (Monthly Sales)
    ai_df['Month'] = ai_df['Date'].dt.to_period('M')
    monthly_sales = ai_df.groupby('Month')['Sales'].sum().reset_index()
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)
    plt.figure(figsize=(10, 4))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
    plt.xticks(rotation=45)
    plt.title('AI: Monthly Sales Trend')
    plt.savefig('ai_time_trend.png')

    # Chart 4: Category Comparison (Bar)
    plt.figure(figsize=(8, 4))
    sns.barplot(data=ai_df, x='Category', y='Sales', estimator=np.sum)
    plt.title('AI: Total Sales by Category')
    plt.savefig('ai_cat_compare.png')

    # Chart 5: Profit vs Sales (Scatter)
    plt.figure(figsize=(8, 4))
    sns.scatterplot(data=ai_df, x='Sales', y='Profit', hue='Category')
    plt.title('AI: Profit vs Sales Relationship')
    plt.savefig('ai_scatter.png')

    # Chart 6: Unusual Chart (Joint Plot with Hex Bins)
    # Why? It shows distribution and correlation simultaneously in a dense, beautiful way.
    g = sns.jointplot(data=ai_df, x='Sales', y='Profit', kind="hex", color="#4CB391")
    g.fig.suptitle("AI: Unusual Hexbin Joint Plot")
    plt.savefig('ai_unusual_joint.png')

    print("AI Script Execution Finished. 6 charts saved.")

# Run the script
run_ai_eda()
# END OF AI GENERATED SCRIPT

# 3. Evaluation
"""
Evaluation Review:
- Are charts labelled? Yes, the AI added standard titles and axis labels automatically via Seaborn/Matplotlib.
- Does the unusual chart add insight? Yes! The Hexbin joint plot is excellent for spotting dense 'sweet spots' 
  where most transactions occur, which is harder to see in a standard scatter plot with 1000 points.
- Portfolio Quality Improvements: 
  1. I would add a consistent color palette (e.g., 'viridis') to make the deck look unified.
  2. I would add annotations to highlight specifically high-performing months or outlier categories.
  3. I would remove the top and right spines (sns.despine()) for a cleaner, modern look.
"""
