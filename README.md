# K-Means Clustering

Customer segmentation using K-Means clustering on mall customer data.

## Overview

This project applies the **K-Means++** algorithm to segment mall customers based on their annual income and spending score. The elbow method is used to determine the optimal number of clusters (k = 5), and results are visualized as a 2D scatter plot.

Implementations are provided in both **Python** and **R**.

## Dataset

**Mall_Customers.csv** — 200 records with the following columns:

| Column | Description |
|---|---|
| CustomerID | Unique identifier |
| Genre | Gender (Male / Female) |
| Age | Customer age |
| Annual Income (k$) | Yearly income in thousands |
| Spending Score (1-100) | Score assigned by the mall |

## Methodology

1. Load the dataset and select features (Annual Income, Spending Score)
2. Run K-Means for k = 1..10 and record WCSS (Within-Cluster Sum of Squares)
3. Plot the elbow curve to identify optimal k
4. Fit K-Means++ with k = 5 and visualize the resulting clusters

![K-Means convergence](https://upload.wikimedia.org/wikipedia/commons/e/ea/K-means_convergence.gif)

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| 🐍 Python 3 | Primary implementation |
| 📊 scikit-learn | KMeans clustering |
| 🔢 NumPy | Numerical operations |
| 📈 Matplotlib | Visualization |
| 🐼 pandas | Data loading |
| 📉 R | Alternative implementation |

## Getting Started

```bash
# Install dependencies
pip install numpy pandas matplotlib scikit-learn

# Run the clustering
python kmeans.py
```

For the R version:

```r
# Requires: cluster package
Rscript kmeans.R
```

## Project Structure

```
├── kmeans.py                      # Python K-Means implementation
├── kmeans.R                       # R K-Means implementation
├── data_preprocessing_template.py # Generic preprocessing template (Python)
├── data_preprocessing_template.R  # Generic preprocessing template (R)
├── Mall_Customers.csv             # Dataset
└── README.md
```

## ⚠️ Known Issues

- `data_preprocessing_template.py` references a generic `Data.csv` that is not included — it is a reusable template, not specific to this project.
- The R script shadows the built-in `kmeans` function by assigning the result to a variable named `kmeans`.
