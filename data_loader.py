import pandas as pd
import numpy as np
from config import DATA_FILE, NUMERIC_COLUMNS

def load_data():
    try:
        df = pd.read_excel(DATA_FILE)
        print(f"✓ Data loaded successfully: {df.shape[0]} countries, {df.shape[1]} features")
        return df
    except FileNotFoundError:
        print(f"✗ Error: {DATA_FILE} not found. Please ensure the CSV file exists.")
        return None

def validate_data(df):
    print("\n" + "="*60)
    print("DATA VALIDATION REPORT")
    print("="*60)
    
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("\n⚠ Missing Values Detected:")
        print(missing[missing > 0])
    else:
        print("\n✓ No missing values detected")
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nDataset Shape:", df.shape)
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    return missing.sum() == 0

def get_summary_statistics(df):
    print("\n" + "="*60)
    print("DESCRIPTIVE STATISTICS")
    print("="*60 + "\n")
    
    stats = df[NUMERIC_COLUMNS].describe().round(3)
    print(stats)
    
    print("\n" + "-"*60)
    print("ADDITIONAL STATISTICS")
    print("-"*60)
    print("\nSkewness (measures asymmetry):")
    print(df[NUMERIC_COLUMNS].skew().round(3))
    print("\nKurtosis (measures tail heaviness):")
    print(df[NUMERIC_COLUMNS].kurtosis().round(3))
    
    return stats
