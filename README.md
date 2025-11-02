# global-happiness-data-analysis

This project explores the relationship between **happiness** and key **socio-economic and environmental indicators** across 80+ countries.  
Using open data from **Numbeo** and the **World Happiness Report 2024**, it applies **data analysis** and **machine learning techniques** to uncover global patterns in well-being.

---

## Dataset Features
- **Countries**: Multiple countries across different continents
- **Metrics**: 8 quality-of-life indicators plus World Happiness Score 2024
  - Purchasing power index
  - Safety index
  - Healthcare index
  - Cost of living index
  - Property price to income ratio
  - Traffic commute time index
  - Pollution index
  - Climate index
  - World Happiness Score 2024

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

## 🧩 Technologies & Libraries
| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Static visualizations |
| **Seaborn** | Statistical graphics |
| **Scikit-learn** | Machine learning (clustering, PCA) |
| **SciPy** | Statistical tests and distributions |

---

## 🧾 Author Notes
This analysis was conducted with attention to:
- Statistical rigor and proper hypothesis testing
- Meaningful interpretation of numerical findings
- Clear communication of insights
- Professional-grade code quality
- Realistic business applications

---

## License
This project was developed **for educational and portfolio purposes only**.  
The dataset used in this analysis was compiled from publicly available summaries on Numbeo (https://www.numbeo.com/quality-of-life/rankings_by_country.jsp) and the **World Happiness Report 2024**.  

The original Numbeo data is **not redistributed** in this repository in accordance with their data usage policy.  
Only derived insights, aggregated results, and visualizations are shared.  

The goal of this project is to demonstrate **data analysis, statistical testing, and clustering techniques** within a real-world socio-economic context — not to reproduce or republish proprietary datasets.
