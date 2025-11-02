import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from config import NUMERIC_COLUMNS, OUTPUTS

def perform_normality_tests(df):
    """Test normality assumption using Shapiro-Wilk test"""
    print("\n" + "="*60)
    print("NORMALITY TESTING (Shapiro-Wilk Test)")
    print("="*60 + "\n")
    
    print("Null Hypothesis: Data is normally distributed")
    print("p-value > 0.05: Likely normal | p-value < 0.05: Likely non-normal\n")
    
    results = {}
    for column in NUMERIC_COLUMNS:
        statistic, p_value = stats.shapiro(df[column])
        is_normal = "✓ Normal" if p_value > 0.05 else "✗ Non-normal"
        print(f"{column:40s} p-value: {p_value:.4f} {is_normal}")
        results[column] = {'statistic': statistic, 'p_value': p_value}
    
    return results

def perform_anova_test(df):
    print("\n" + "="*60)
    print("HOMOGENEITY OF VARIANCE TEST (Levene's Test)")
    print("="*60 + "\n")
    
    normalized = df[NUMERIC_COLUMNS].apply(lambda x: (x - x.mean()) / x.std())
    
    statistic, p_value = stats.levene(*[normalized[col] for col in NUMERIC_COLUMNS])
    
    print(f"Levene's Test Statistic: {statistic:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value > 0.05:
        print("✓ Variances are homogeneous across metrics")
    else:
        print("✗ Variances are NOT homogeneous across metrics")

def analyze_skewness_kurtosis(df):
    """Detailed skewness and kurtosis analysis"""
    print("\n" + "="*60)
    print("DETAILED DISTRIBUTION SHAPE ANALYSIS")
    print("="*60 + "\n")
    
    for column in NUMERIC_COLUMNS:
        skewness = df[column].skew()
        kurtosis = df[column].kurtosis()
        
        if abs(skewness) < 0.5:
            skew_type = "Fairly Symmetric"
        elif skewness > 0:
            skew_type = "Right-skewed (positive tail)"
        else:
            skew_type = "Left-skewed (negative tail)"
        
        if abs(kurtosis) < 1:
            kurt_type = "Mesokurtic (normal)"
        elif kurtosis > 1:
            kurt_type = "Leptokurtic (heavy tails)"
        else:
            kurt_type = "Platykurtic (light tails)"
        
        print(f"\n{column}:")
        print(f"  Skewness: {skewness:7.3f} - {skew_type}")
        print(f"  Kurtosis: {kurtosis:7.3f} - {kurt_type}")
