"""
Day 16 · PM Session · Take-Home Assignment
Part B — Stretch Problem: Interactive Charts with Plotly Express
"""

import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load the same dataset
df = pd.read_csv('eda_assignment_data.csv')

# 1. Interactive Distribution Plot (Age)
fig1 = px.histogram(df, x="Age", marginal="rug", title="Interactive Distribution of Age",
                   labels={'Age':'Customer Age'}, opacity=0.7)
fig1.write_html("interactive_age_dist.html")
print("Saved interactive_age_dist.html")

# 2. Interactive Scatter Plot (Income vs Spending Score with Gender tagging)
fig2 = px.scatter(df, x="AnnualIncome", y="SpendingScore", color="Gender", 
                 title="Interactive Income vs Spending Score",
                 labels={'AnnualIncome':'Annual Income ($)', 'SpendingScore':'Spending Score (1-100)'},
                 hover_data=['Age', 'Region'])
fig2.write_html("interactive_income_spending.html")
print("Saved interactive_income_spending.html")

# 3. Interactive Box Plot (Income across Regions)
fig3 = px.box(df, x="Region", y="AnnualIncome", color="Region", 
             title="Interactive Regional Income Distribution",
             points="all") # Show all points to see data density
fig3.write_html("interactive_regional_income.html")
print("Saved interactive_regional_income.html")

# Identification of 2 types of insights easier to see in interactive charts:
"""
Type 1: Outlier Identification and Investigation
In a static box plot, outliers are just dots. In an interactive Plotly chart, I can hover over an outlier 
to immediately see its CustomerID, Age, and other attributes, allowing for instant data validation.

Type 2: Local Trends in Dense Data
In a scatter plot with 1200 points, static overlaps make it hard to see individual values. 
With interactivity, I can zoom into specific clusters (e.g., high-income, high-spending) 
and use the hover tool to differentiate between overlapping points accurately.
"""
