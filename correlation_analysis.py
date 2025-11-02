import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from config import NUMERIC_COLUMNS, OUTPUTS, CORRELATION_THRESHOLD

def analyze_correlations(df):
    print("\n" + "="*60)
    print("CORRELATION ANALYSIS")
    print("="*60 + "\n")
    
    pearson_corr = df[NUMERIC_COLUMNS].corr(method='pearson')
    
    spearman_corr = df[NUMERIC_COLUMNS].corr(method='spearman')
    
    print("STRONGEST POSITIVE CORRELATIONS (Pearson):")
    print("-" * 60)
    
    corr_pairs = []
    for i in range(len(pearson_corr.columns)):
        for j in range(i+1, len(pearson_corr.columns)):
            corr_pairs.append((
                pearson_corr.columns[i],
                pearson_corr.columns[j],
                pearson_corr.iloc[i, j]
            ))
    
    corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    
    for var1, var2, corr_val in corr_pairs[:10]:
        if abs(corr_val) >= CORRELATION_THRESHOLD:
            interpretation = "STRONG"
        elif abs(corr_val) >= 0.5:
            interpretation = "MODERATE"
        else:
            interpretation = "WEAK"
        
        print(f"{var1} <-> {var2}")
        print(f"  Correlation: {corr_val:.3f} ({interpretation})")
        print()
    
    return pearson_corr, spearman_corr

def visualize_correlation_matrix(df, pearson_corr):
    fig, ax = plt.subplots(figsize=(14, 12))
    
    sns.heatmap(pearson_corr, annot=True, fmt='.2f', cmap='RdBu_r', 
                center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.8},
                ax=ax, vmin=-1, vmax=1)
    
    ax.set_title('Correlation Matrix: All Metrics', fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'{OUTPUTS["plots"]}/02_correlation_matrix.png', dpi=300, bbox_inches='tight')
    print("✓ Correlation matrix visualization saved")
    plt.close()

def analyze_happiness_drivers(df):
    print("\n" + "="*60)
    print("HAPPINESS DRIVERS ANALYSIS")
    print("="*60 + "\n")
    
    happiness_corr = df[NUMERIC_COLUMNS].corrwith(df['WorldHappinessScore_2024']).sort_values(ascending=False)
    
    print("Correlation with World Happiness Score 2024:\n")
    for metric, corr_val in happiness_corr.items():
        if metric != 'WorldHappinessScore_2024':
            bar = "█" * int(abs(corr_val) * 20)
            direction = "↑" if corr_val > 0 else "↓"
            print(f"{metric:35s} {direction} {corr_val:6.3f} {bar}")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    happiness_corr = happiness_corr.drop('WorldHappinessScore_2024')
    colors = ['green' if x > 0 else 'red' for x in happiness_corr.values]
    
    happiness_corr.plot(kind='barh', ax=ax, color=colors, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Correlation Coefficient', fontsize=12, fontweight='bold')
    ax.set_title('What Drives Happiness? Correlation Analysis', fontsize=14, fontweight='bold')
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUTS["plots"]}/03_happiness_drivers.png', dpi=300, bbox_inches='tight')
    print("✓ Happiness drivers visualization saved")
    plt.close()
