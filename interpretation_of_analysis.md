# 📘 Interpretation of analysis

This document summarizes the analytical findings of the **Global Happiness and Quality of Life dataset**, including distribution analysis, outlier detection, correlation insights, and clustering results.

---

## 🧩 Data overview

The dataset was validated, and no missing values were found.  
Basic statistics (count, mean, standard deviation, min, max, quartiles) were computed for all numeric indicators.

---

## 📊 Distribution analysis

Distribution plots were generated for all numerical indicators using a custom Python function (`analyze_distributions`).  
Each plot included vertical reference lines for the **mean** (red dashed) and **median** (green dashed).

These visualizations provided insights into data symmetry, spread, and potential outliers.

- Most variables are approximately normal — suitable for regression or clustering.
- **Property price to income ratio** is the only extreme outlier (highly right-skewed and leptokurtic).
- **Climate**, **Traffic**, and **Pollution** show slight non-normality but remain interpretable.
- Overall, the dataset reflects moderate variability, limited outliers, and balanced structure.

---

## ⚖️ Skewness Analysis

| Indicator | Skewness | Interpretation |
|------------|-----------|----------------|
| Pollution index | -0.274 | Shows a mild left skew, indicating that most countries have moderate to high pollution levels, with only a few reporting very low pollution. |
| Health care index | -0.251 | Slightly left-skewed, meaning healthcare quality tends to be higher in most countries, with fewer cases of very low scores. |
| Climate index | -1.278 | Strongly left-skewed, suggesting that many countries experience relatively favorable climate conditions, while only a few face much lower climate scores. |
| Purchasing power index | 0.451 | Mild right skew, showing that most countries have moderate purchasing power, but a few have significantly higher values. |
| Safety index | -0.474 | Slightly left-skewed, indicating that a larger share of countries reports higher safety levels, with fewer recording very low safety. |
| Property price to income ratio | 2.472 | Strong right skew, meaning housing affordability is generally within a normal range, but a few countries have extremely high property-to-income ratios. |
| World Happiness Score 2024 | -0.878 | Moderately left-skewed, showing that most countries report medium to high levels of happiness, with relatively few at the lower end. |
| Traffic commute time index | 0.908 | Moderately right-skewed, meaning commuting times are typically reasonable, though a small number of cases show considerably longer travel times. |
| Cost of living index | 0.807 | Moderately right-skewed, indicating that living costs are average in most countries, but a few have noticeably higher expenses. |

**Conclusion:**  
Most variables are approximately normal. Exceptions include *Property price to income ratio* (highly right-skewed) and *Climate index* (moderately left-skewed), suggesting outlier countries. The dataset remains well-behaved statistically.

---

## 🏔️ Kurtosis Analysis

| Indicator | Kurtosis | Interpretation |
|------------|-----------|----------------|
| Pollution index | -1.064 | Low kurtosis indicates a flat distribution, meaning pollution levels are fairly evenly spread across countries, with few extreme outliers. |
| Health care index | -0.345 | Slightly flatter than normal, suggesting that healthcare scores are moderately consistent, with limited extreme highs or lows. |
| Climate index | 2.015 | Leptokurtic (peaked) distribution; most countries cluster closely around similar climate conditions, but a few exhibit more extreme values on either side. |
| Purchasing power index | -0.639 | Low kurtosis, meaning purchasing power is relatively uniform across countries, with few extreme variations. |
| Safety index | -0.002 | Very close to normal distribution; safety levels are evenly distributed, without noticeable extremes. |
| Property price to income ratio | 9.996 | Extremely high kurtosis, showing that this indicator has significant outliers. A few countries have property prices far above the typical range, making this variable highly concentrated around the mean with rare but extreme deviations. |
| World Happiness Score 2024 | 0.755 | Slightly peaked distribution, suggesting most happiness scores cluster around the average, with some higher or lower outliers. |
| Traffic commute time index | 1.345 | Moderately high kurtosis; commuting times are similar for most countries, but a few show unusually high or low values. |
| Cost of living index | 0.642 | Mildly peaked distribution; most observations are centered near the mean, with only limited variation at the extremes. |

**Conclusion:**  
Most indicators have kurtosis near or below zero, meaning balanced, well-spread distributions.  
Only *Property price to income ratio*, *Climate*, and *Traffic* indices show high kurtosis, indicating the presence of strong outliers.

---

## 🚦 Outlier Analysis (IQR Method)

| Indicator | Bounds | Outliers Found | Countries |
|------------|---------|----------------|------------|
| Traffic commute time index | [12.75, 56.35] | 3 | Costa Rica, Nigeria, Bangladesh |
| Cost of living index | [-10.95, 101.45] | 1 | Switzerland |
| Safety index | [25.50, 95.10] | 2 | Venezuela, South Africa |
| Property price to income ratio | [-1.00, 25.40] | 4 | Vietnam, Hong Kong, Nigeria, Sri Lanka |
| World Happiness Score 2024 | [3.55, 8.64] | 1 | Lebanon |
| Climate index | [38.55, 122.15] | 2 | Kuwait, Russia |

**Interpretation:**
- Long commute outliers (Costa Rica, Nigeria, Bangladesh) indicate congestion and transport inefficiency.  
- Switzerland shows exceptionally high cost of living.  
- Venezuela and South Africa display unusually low safety.  
- Property affordability extremes exist in Nigeria, Sri Lanka, Hong Kong, and Vietnam.  
- Lebanon has the lowest happiness score.  
- Kuwait and Russia experience extreme climate variations.

---

## 🥇 Top & Bottom Performers

| Indicator | Top 3 Countries | Bottom 3 Countries |
|------------|------------------|--------------------|
| **Purchasing power index** | Kuwait, Switzerland, Luxembourg | Nigeria, Venezuela, Sri Lanka |
| **Traffic commute time index** | Nigeria, Costa Rica, Bangladesh | Iceland, Estonia, Netherlands |
| **Health care index** | Taiwan, South Korea, Netherlands | Venezuela, Bangladesh, Morocco |
| **Cost of living index** | Switzerland, Iceland, Singapore | Pakistan, India, Egypt |
| **Safety index** | UAE, Taiwan, Hong Kong | Venezuela, South Africa, Peru |
| **Property price to income ratio** | Nigeria, Sri Lanka, Hong Kong | South Africa, USA, Saudi Arabia |
| **World Happiness Score 2024** | Finland, Denmark, Iceland | Lebanon, Bangladesh, Sri Lanka |
| **Climate index** | Uruguay, Malta, Portugal | Kuwait, Russia, Kazakhstan |
| **Pollution index** | Lebanon, Nigeria, Bangladesh | Finland, Iceland, Estonia |

**Interpretation:**  
The ranking analysis shows strong contrasts between nations — wealthier countries generally achieve higher happiness, safety, and health outcomes, while lower-income or environmentally stressed countries face multidimensional challenges.

---

## 🔗 Correlation Analysis

The `analyze_correlations()` function computes **Pearson** and **Spearman** correlations between all numeric variables.

| Pair | Correlation | Interpretation |
|------|--------------|----------------|
| Purchasing Power ↔ Cost of Living | 0.766 (Strong) | Wealthier countries face higher living costs. |
| Cost of Living ↔ Pollution | -0.753 (Strong) | Higher costs associate with lower pollution — developed nations cleaner. |
| Happiness ↔ Pollution | -0.727 (Strong) | Higher pollution strongly reduces happiness. |
| Purchasing Power ↔ Happiness | 0.703 (Strong) | Higher income correlates with higher happiness. |
| Cost of Living ↔ Happiness | 0.691 (Moderate) | Reflects higher development levels. |
| Purchasing Power ↔ Pollution | -0.664 (Moderate) | Richer countries tend to be less polluted. |
| Health Care ↔ Pollution | -0.563 (Moderate) | Better healthcare coincides with cleaner environments. |
| Traffic Time ↔ Pollution | 0.541 (Moderate) | Congestion increases pollution. |
| Purchasing Power ↔ Health Care | 0.527 (Moderate) | Economic strength supports better healthcare. |
| Traffic Time ↔ Happiness | -0.527 (Moderate) | Longer commutes reduce happiness. |

**Summary:**  
Happiness increases with economic prosperity, healthcare quality, and safety, while pollution, commuting time, and poor housing affordability have negative effects.

---

## 🧮 Normality Test (Shapiro–Wilk)

| Indicator | p-value | Normality |
|------------|----------|------------|
| Purchasing Power | 0.0066 | ✗ Non-normal |
| Traffic Commute Time | 0.0027 | ✗ Non-normal |
| Health Care | 0.7203 | ✓ Normal |
| Cost of Living | 0.0027 | ✗ Non-normal |
| Safety | 0.0645 | ✓ Normal |
| Property Price to Income Ratio | 0.0000 | ✗ Non-normal |
| World Happiness Score | 0.0022 | ✗ Non-normal |
| Climate | 0.0000 | ✗ Non-normal |
| Pollution | 0.0038 | ✗ Non-normal |

**Interpretation:**  
Only *Health Care* and *Safety* follow normal distribution. Most other indicators deviate significantly, consistent with skewness and kurtosis findings.

---

## 📏 Homogeneity of Variance (Levene’s Test)

| Test | Statistic | p-value | Result |
|------|------------|----------|---------|
| Levene’s Test | 0.755 | 0.6428 | ✓ Variances are homogeneous |

**Interpretation:**  
Variance across indicators is consistent, meeting the assumption of homogeneity — useful for comparative and clustering analysis.

---

## 🧭 Clustering Analysis Summary

### `perform_clustering(df)`
- Standardizes all numeric variables.  
- Tests multiple cluster counts using **Elbow** and **Silhouette** methods.  
- Trains the final K-Means model and evaluates with **Silhouette** and **Davies–Bouldin** scores.

**Result:**  
`k = 4` was selected — the Elbow curve flattens here (diminishing returns), and Silhouette score remains stable, indicating balanced separation.

### `analyze_cluster_characteristics(df)`
- Calculates mean values per indicator for each cluster.  
- Compares with global averages to describe socio-economic profiles.

### `visualize_clusters(df, X_scaled)`
- Uses **PCA (Principal Component Analysis)** for 3D visualization of country clusters.

---

# 🌍 Key Insights from the Global Happiness and Quality of Life Analysis

---

## 💰 Economic Insights

1. **Money matters — but not alone.**  
   Purchasing power shows the strongest positive correlation with happiness (**r = 0.70**).  
   Higher income levels tend to increase life satisfaction, but wealth improves happiness only when combined with safety, healthcare, and stability.

2. **The cost of comfort.**  
   Countries with higher purchasing power also face higher living costs (**r = 0.77**).  
   Economic prosperity often comes with higher expenses — comfort has a financial trade-off.

3. **Housing inequality is striking.**  
   The *property price-to-income ratio* shows extreme right skewness (2.47) and high kurtosis (9.99).  
   A few countries experience **severe housing unaffordability**, highlighting global inequality in property markets.

---

## 🏥 Social and Well-Being Insights

4. **Health and safety are silent happiness drivers.**  
   Healthcare (**r = 0.49**) and safety (**r = 0.29**) correlate positively with happiness.  
   Societies that invest in healthcare and personal safety achieve higher well-being.

5. **Unhappy commute, unhappy life.**  
   The *traffic commute time index* correlates negatively with happiness (**r = -0.53**).  
   Longer, stressful commutes reduce life satisfaction, showing how urban design impacts happiness.

6. **Lebanon’s sharp contrast.**  
   Lebanon is a major outlier — lowest happiness score (2.71) and highest pollution level (89.6).  
   Economic instability and environmental stress strongly impact well-being.

---

## 🌱 Environmental Insights

7. **Pollution is the strongest negative factor.**  
   Happiness and pollution are strongly inversely correlated (**r = -0.73**).  
   Cleaner environments consistently align with higher happiness levels.

8. **Climate comfort matters — but less than expected.**  
   The *climate index* has only a weak correlation with happiness.  
   Favorable weather alone does not make nations happier, though extreme climates lower satisfaction.

9. **The cleaner, the happier.**  
   Cost of living and pollution have a strong **negative correlation (-0.75)** —  
   wealthier countries tend to invest in environmental quality, combining prosperity with cleaner living conditions.

---

## 🌎 Cluster-Based Insights (K-Means, k=4)

10. **Four global profiles emerged:**

| Cluster | General Profile | Key Characteristics |
|----------|-----------------|---------------------|
| **1️⃣ High-Income & Happy** | Wealthy, safe, low-pollution countries | High happiness, excellent healthcare, high living costs |
| **2️⃣ Affordable but Polluted** | Low-cost regions with environmental and infrastructure challenges | Lower happiness, high pollution, long commutes |
| **3️⃣ Safe & Balanced** | Moderate-income, stable societies | Balanced happiness, good safety, average costs |
| **4️⃣ Developing with Challenges** | Economically and environmentally strained nations | Lowest happiness, poor affordability, high pollution |

These clusters reveal that happiness is **multidimensional**, shaped by the balance between **economy, safety, health, and environment**.

---

## 📈 Global Takeaways

11. **Economic growth doesn’t guarantee happiness** — social and environmental well-being are equally important.  
12. **Environmental sustainability and happiness are deeply connected** — clean air and livable cities matter as much as income.  
13. **Happiness is holistic** — it emerges where **economic strength**, **social safety**, and **environmental quality** coexist.

---

## 💡 In One Sentence

> The happiest countries are not necessarily the richest — they are the ones that balance prosperity, safety, and a clean, livable environment.

---


