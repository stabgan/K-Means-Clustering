# K-Means Clustering

# Importing the libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def main():
    # Importing the dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = pd.read_csv(os.path.join(script_dir, "Mall_Customers.csv"))
    X = dataset.iloc[:, [3, 4]].values

    # Using the elbow method to find the optimal number of clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(
            n_clusters=i, init="k-means++", n_init=10, random_state=42
        )
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.figure()
    plt.plot(range(1, 11), wcss, marker="o")
    plt.title("The Elbow Method")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.tight_layout()
    plt.show()

    # Fitting K-Means to the dataset
    kmeans = KMeans(
        n_clusters=5, init="k-means++", n_init=10, random_state=42
    )
    y_kmeans = kmeans.fit_predict(X)

    # Visualising the clusters
    plt.figure(figsize=(10, 6))
    colors = ["red", "blue", "green", "cyan", "magenta"]
    labels = [
        "Careful", "Standard", "Target", "Careless", "Sensible"
    ]
    for idx, (color, label) in enumerate(zip(colors, labels)):
        plt.scatter(
            X[y_kmeans == idx, 0],
            X[y_kmeans == idx, 1],
            s=100,
            c=color,
            label=f"Cluster {idx + 1} ({label})",
        )

    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s=300,
        c="yellow",
        edgecolors="black",
        label="Centroids",
    )
    plt.title("Clusters of Customers")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
