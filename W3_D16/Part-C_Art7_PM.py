"""
Day 16 · PM Session · Take-Home Assignment
Part C — Interview Ready
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

# Q1 — When would you use a violin plot instead of a box plot? What additional information does it show?
"""
Answer:
You should use a violin plot when you want to see the underlying distribution (density) of the data, 
not just the summary statistics (quartiles, median). 
While a box plot shows only the "skeleton" of the data, a violin plot shows the "shape."
Additional information:
- Bimodality: It reveals if the data has two peaks, which a box plot might hide.
- Skewness: The width of the violin at different points shows where the data is concentrated.
"""

# Q2 (Coding) — Implement plot_numerical_eda(df)
def plot_numerical_eda(df):
    """
    Produces a 1x3 panel (Histogram, Box plot, QQ plot) for every numerical column.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        fig.suptitle(f'Numerical EDA for {col}', fontsize=16)
        
        # 1. Histogram
        sns.histplot(df[col], kde=True, ax=axes[0], color='blue')
        axes[0].set_title('Histogram + KDE')
        
        # 2. Box Plot
        sns.boxplot(y=df[col], ax=axes[1], color='orange')
        axes[1].set_title('Box Plot')
        
        # 3. QQ Plot
        stats.probplot(df[col].dropna(), dist="norm", plot=axes[2])
        axes[2].set_title('Normal Q-Q Plot')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save the specific plot (naming based on column)
        filename = f'eda_{col}.png'
        plt.savefig(filename)
        plt.close() # Close to avoid memory issues with many columns
        print(f"Saved {filename}")

# Test with a small subset to verify
df_sample = pd.read_csv('eda_assignment_data.csv')[['Age', 'AnnualIncome']]
plot_numerical_eda(df_sample)


# Q3 (Critique) — Chart choices
"""
(a) A 3D pie chart with 12 segments for market share.
    Problem: 3D perspective distorts the slices (making the front one look larger than it is). 
             12 segments are too many for the human eye to compare easily in a circle.
    Alternative: A horizontal Bar Chart sorted from highest to lowest market share.

(b) A line chart for survey scores across 5 unordered categories.
    Problem: A line implies a trend or temporal sequence (continuity) between categories. 
             Connecting "North" to "South" with a line is misleading.
    Alternative: A Bar Chart or Box Plot (if you want to see distribution).

(c) A scatter plot with 500k points and no transparency.
    Problem: Overplotting. The chart will likely look like a solid blob of ink, hiding the 
             density and the actual relationship between variables.
    Alternative: Use 'alpha' transparency, or better yet, a Hexbin plot or a 2D Histogram (Density plot).
"""
