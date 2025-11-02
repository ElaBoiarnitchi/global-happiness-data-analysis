import os
import pandas as pd
from config import OUTPUTS
from data_loader import load_data, validate_data, get_summary_statistics
from eda_analysis import analyze_distributions, analyze_outliers, analyze_top_bottom_performers
from correlation_analysis import analyze_correlations, visualize_correlation_matrix, analyze_happiness_drivers
from statistical_tests import perform_normality_tests, perform_anova_test, analyze_skewness_kurtosis
from clustering_analysis import perform_clustering, analyze_cluster_characteristics, visualize_clusters

for dir_path in OUTPUTS.values():
    os.makedirs(dir_path, exist_ok=True)

def main():
    """Execute complete analysis pipeline"""
    print("\n" + "="*60)
    print("PROFESSIONAL DATA ANALYSIS PIPELINE")
    print("Global Country Metrics Analysis")
    print("="*60)
    
    # 1. Load and validate data
    print("\n[1/6] Loading and validating data...")
    df = load_data()
    if df is None:
        return
    
    validate_data(df)
    get_summary_statistics(df)
    
    # 2. Exploratory Data Analysis
    print("\n[2/6] Performing exploratory data analysis...")
    analyze_distributions(df)
    analyze_outliers(df)
    analyze_top_bottom_performers(df)
    
    # 3. Correlation Analysis
    print("\n[3/6] Analyzing correlations and relationships...")
    pearson_corr, spearman_corr = analyze_correlations(df)
    visualize_correlation_matrix(df, pearson_corr)
    analyze_happiness_drivers(df)
    
    # 4. Statistical Tests
    print("\n[4/6] Performing statistical hypothesis tests...")
    perform_normality_tests(df)
    perform_anova_test(df)
    analyze_skewness_kurtosis(df)
    
    # 5. Clustering Analysis
    print("\n[5/6] Performing clustering analysis...")
    df_clustered, X_scaled, kmeans = perform_clustering(df)
    analyze_cluster_characteristics(df_clustered)
    visualize_clusters(df_clustered, X_scaled)
    
    # 6. Save processed data
    print("\n[6/6] Saving analysis results...")
    df_clustered.to_csv(f'{OUTPUTS["data"]}/countries_with_clusters.csv', index=False)
    print("✓ Clustered data saved")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print(f"\nOutputs generated:")
    print(f"  ✓ Visualizations: {OUTPUTS['plots']}")
    print(f"  ✓ Reports: {OUTPUTS['reports']}")
    print(f"  ✓ Data: {OUTPUTS['data']}")
    print("\nNext steps:")
    print("  1. Review generated plots and identify insights")
    print("  2. Examine cluster characteristics for patterns")
    print("  3. Validate findings with domain knowledge")
    print("  4. Build predictive models if needed")
    print("\n")

if __name__ == "__main__":
    main()
