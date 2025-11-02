# global-happiness-data-analysis

This project explores the relationship between **happiness** and key **socio-economic and environmental indicators** across 80+ countries.  
Using open data from **Numbeo** and the **World Happiness Report 2024**, it applies **data analysis** and **machine learning techniques** to uncover global patterns in well-being.

---

## 🎯 Objectives
1. Explore the relationships between happiness and socio-economic indicators.
2. Examine data distribution characteristics (skewness, kurtosis, outliers).
3. Test statistical assumptions such as normality and homogeneity of variance.
4. Identify key happiness drivers through correlation analysis.
5. Group countries into clusters with similar life-quality profiles using **K-Means**.
6. Visualize global patterns through distribution, correlation, and clustering plots.

---

## 🧠 Methodology
The project follows a structured six-step analysis workflow:
1. Load and validate data — Import and check dataset integrity, missing values, and descriptive statistics.
2. Exploratory data analysis (EDA) — Analyze distributions, detect outliers, and compare top and bottom performers.
3. Correlation analysis — Compute Pearson and Spearman coefficients to identify relationships between indicators and happiness; visualize through heatmaps.
4. Statistical hypothesis testing — Apply Shapiro–Wilk for normality, ANOVA for mean comparison, and Levene’s test for variance homogeneity.
5. Clustering analysis — Perform K-Means clustering on standardized data, determine optimal k using Elbow and Silhouette methods, and visualize results with 3D PCA.
6. Result export — Save clustered data and visual outputs for interpretation and reporting.

---

## 🧩 Tools and Technologies
- **Python**: pandas, numpy, scikit-learn, scipy, sklearn
- **Statistical Analysis**: correlation, Shapiro–Wilk, Levene’s test  
- **Machine Learning**: K-Means, PCA  
- **Visualization**: matplotlib, seaborn, 3D PCA plots  

---

## Key Technical Skills Demonstrated
✅ **Data Manipulation**: Pandas for cleaning, transformation, and aggregation
✅ **Statistical Analysis**: Scipy for hypothesis testing and distributions
✅ **Machine Learning**: Scikit-learn for clustering and dimensionality reduction
✅ **Visualization**: Matplotlib & Seaborn for publication-quality graphics
✅ **Professional Coding**: Modular design, configuration management, error handling
✅ **Data Interpretation**: Translating statistical findings into actionable insights
