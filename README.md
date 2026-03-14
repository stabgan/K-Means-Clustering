# K-Means Clustering — Customer Segmentation

A machine-learning project that segments mall customers into distinct groups based on their **Annual Income** and **Spending Score** using the K-Means clustering algorithm. Implementations are provided in both Python and R.

## Methodology

### 1. Elbow Method

The optimal number of clusters is determined using the **Elbow Method**. We compute the Within-Cluster Sum of Squares (WCSS) for cluster counts 1 through 10 and plot the results. The "elbow" in the curve indicates the point of diminishing returns — in this dataset, **K = 5** is the sweet spot.

### 2. K-Means++ Clustering

Once the optimal K is identified, the K-Means++ algorithm is applied to avoid the random initialization trap. The algorithm:

1. Selects K initial centroids using a smart seeding strategy.
2. Assigns each data point to the nearest centroid (Euclidean distance).
3. Recomputes centroids as the mean of each cluster.
4. Repeats steps 2–3 until convergence.

The result is five well-separated customer segments visualized in a scatter plot.

![K-Means convergence](https://upload.wikimedia.org/wikipedia/commons/e/ea/K-means_convergence.gif)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| 🐍 Language | Python 3, R |
| 📊 Data | pandas, NumPy |
| 🤖 ML | scikit-learn (`KMeans`) |
| 📈 Visualization | matplotlib (Python), `cluster` package (R) |

## Dependencies

### Python

```
numpy
matplotlib
pandas
scikit-learn
```

### R

```
cluster
caTools
```

## How to Run

### Python

```bash
# Install dependencies
pip install numpy matplotlib pandas scikit-learn

# Run the clustering script
python kmeans.py
```

### R

```r
# Open kmeans.R in RStudio or run from the terminal
Rscript kmeans.R
```

> The dataset `Mall_Customers.csv` must be in the same directory as the scripts.

## Dataset

`Mall_Customers.csv` contains 200 records with features including Customer ID, Gender, Age, Annual Income (k$), and Spending Score (1–100). The clustering uses only Annual Income and Spending Score.

## Known Issues

- `data_preprocessing_template.py` references a generic `Data.csv` that is not included in this repository — it is a standalone preprocessing template, not part of the clustering pipeline.
- The R scripts use base `kmeans()` without K-Means++ initialization (R's default is Hartigan-Wong).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
