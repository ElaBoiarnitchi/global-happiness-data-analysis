import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from config import NUMERIC_COLUMNS, OUTPUTS

def analyze_distributions(df):
    print("\n" + "="*60)
    print("DISTRIBUTION ANALYSIS")
    print("="*60 + "\n")
    
    fig, axes = plt.subplots(4, 3, figsize=(16, 14))
    axes = axes.ravel()
    
    for idx, column in enumerate(NUMERIC_COLUMNS):
        axes[idx].hist(df[column], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribution of {column}', fontweight='bold')
        axes[idx].set_xlabel('Value')
        axes[idx].set_ylabel('Frequency')
        
        mean = df[column].mean()
        median = df[column].median()
        axes[idx].axvline(mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean:.1f}')
        axes[idx].axvline(median, color='green', linestyle='--', linewidth=2, label=f'Median: {median:.1f}')
        axes[idx].legend(fontsize=8)
        axes[idx].grid(alpha=0.3)
    
    fig.delaxes(axes[-1])
    plt.tight_layout()
    plt.savefig(f'{OUTPUTS["plots"]}/01_distributions.png', dpi=300, bbox_inches='tight')
    print("✓ Distribution plots saved")
    plt.close()

def analyze_outliers(df):
    print("\n" + "="*60)
    print("OUTLIER ANALYSIS (IQR Method)")
    print("="*60 + "\n")
    
    outliers_dict = {}
    
    for column in NUMERIC_COLUMNS:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        
        if len(outliers) > 0:
            outliers_dict[column] = outliers
            print(f"\n{column}:")
            print(f"  Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
            print(f"  Outliers found: {len(outliers)}")
            print(f"  Countries: {', '.join(outliers['Country'].tolist())}")
    
    if not outliers_dict:
        print("✓ No significant outliers detected")
    
    return outliers_dict

def analyze_top_bottom_performers(df):
    print("\n" + "="*60)
    print("TOP & BOTTOM PERFORMERS BY METRIC")
    print("="*60 + "\n")
    
    for column in NUMERIC_COLUMNS:
        print(f"\n{column}:")
        print("  Top 3 Countries:")
        top = df.nlargest(3, column)[['Country', column]]
        for idx, (_, row) in enumerate(top.iterrows(), 1):
            print(f"    {idx}. {row['Country']}: {row[column]:.2f}")
        
        print("  Bottom 3 Countries:")
        bottom = df.nsmallest(3, column)[['Country', column]]
        for idx, (_, row) in enumerate(bottom.iterrows(), 1):
            print(f"    {idx}. {row['Country']}: {row[column]:.2f}")
