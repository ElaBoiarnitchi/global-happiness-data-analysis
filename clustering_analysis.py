import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from config import NUMERIC_COLUMNS, OUTPUTS, N_CLUSTERS, RANDOM_STATE

def perform_clustering(df):
    """Perform K-means clustering on normalized data"""
    print("\n" + "="*60)
    print("CLUSTERING ANALYSIS (K-Means)")
    print("="*60 + "\n")
    
    X = df[NUMERIC_COLUMNS].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    inertias = []
    silhouette_scores = []
    K_range = range(2, 10)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Number of Clusters (k)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Inertia', fontsize=12, fontweight='bold')
    ax1.set_title('Elbow Method: Optimal k Selection', fontsize=13, fontweight='bold')
    ax1.grid(alpha=0.3)
    ax1.axvline(x=N_CLUSTERS, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'Selected k={N_CLUSTERS}')
    ax1.legend()
    
    ax2.plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
    ax2.set_xlabel('Number of Clusters (k)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Silhouette Score', fontsize=12, fontweight='bold')
    ax2.set_title('Silhouette Score: Cluster Quality', fontsize=13, fontweight='bold')
    ax2.grid(alpha=0.3)
    ax2.axvline(x=N_CLUSTERS, color='red', linestyle='--', linewidth=2, alpha=0.7)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUTS["plots"]}/04_elbow_silhouette.png', dpi=300, bbox_inches='tight')
    print("✓ Elbow and silhouette plots saved")
    plt.close()
    
    final_kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=RANDOM_STATE, n_init=10)
    clusters = final_kmeans.fit_predict(X_scaled)
    
    silhouette_avg = silhouette_score(X_scaled, clusters)
    davies_bouldin = davies_bouldin_score(X_scaled, clusters)
    
    print(f"\nOptimal number of clusters: {N_CLUSTERS}")
    print(f"Silhouette Score: {silhouette_avg:.3f} (closer to 1 is better)")
    print(f"Davies-Bouldin Score: {davies_bouldin:.3f} (lower is better)")
    
    df['Cluster'] = clusters
    return df, X_scaled, final_kmeans

def analyze_cluster_characteristics(df):
    print("\n" + "="*60)
    print("CLUSTER PROFILES & INTERPRETATIONS")
    print("="*60 + "\n")
    
    for cluster_id in range(N_CLUSTERS):
        cluster_data = df[df['Cluster'] == cluster_id]
        print(f"\n{'='*60}")
        print(f"CLUSTER {cluster_id}: {len(cluster_data)} countries")
        print(f"{'='*60}")
        
        print("\nCountries in this cluster:")
        countries = cluster_data['Country'].tolist()
        print(", ".join(countries[:10]) + ("..." if len(countries) > 10 else ""))
        
        print("\nCluster Profile (Mean Values):")
        print("-" * 60)
        
        profile = cluster_data[NUMERIC_COLUMNS].mean()
        overall_mean = df[NUMERIC_COLUMNS].mean()
        
        for metric in NUMERIC_COLUMNS:
            cluster_val = profile[metric]
            overall_val = overall_mean[metric]
            diff_pct = ((cluster_val - overall_val) / overall_val * 100) if overall_val != 0 else 0
            
            comparison = "ABOVE" if cluster_val > overall_val else "BELOW"
            print(f"{metric:40s} {cluster_val:7.2f} ({comparison} avg by {abs(diff_pct):5.1f}%)")
        
        happiness_mean = cluster_data['WorldHappinessScore_2024'].mean()
        print(f"\nAverage Happiness Score: {happiness_mean:.2f}")

def visualize_clusters(df, X_scaled):
    """Create 3D visualization of clusters"""
    fig = plt.figure(figsize=(14, 10))
    
    from sklearn.decomposition import PCA
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(X_scaled)
    
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['red', 'blue', 'green', 'orange', 'purple'][:N_CLUSTERS]
    
    for cluster_id in range(N_CLUSTERS):
        cluster_mask = df['Cluster'] == cluster_id
        ax.scatter(X_pca[cluster_mask, 0], X_pca[cluster_mask, 1], X_pca[cluster_mask, 2],
                  c=colors[cluster_id], label=f'Cluster {cluster_id}', s=100, alpha=0.7, edgecolors='black')
    
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})', fontweight='bold')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})', fontweight='bold')
    ax.set_zlabel(f'PC3 ({pca.explained_variance_ratio_[2]:.1%})', fontweight='bold')
    ax.set_title('Country Clustering: 3D PCA Visualization', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUTS["plots"]}/05_cluster_3d_visualization.png', dpi=300, bbox_inches='tight')
    print("✓ 3D cluster visualization saved")
    plt.close()
