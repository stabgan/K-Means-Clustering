# K-Means-Clustering
I implemented the K-Means Clustering Model to Analyse the Data in Python and R

## The steps I followed are :
- Choose the number K of the clusters
- Select at random K points , the centroids ( not necessarily from your dataset )
- Assign each data point to the closest centroid - That forms K cluster [ We basically take Eucleidan distance ]
- Compute and place the new centroid of each Cluster
- Reassign each data point to the new closest centroid 
-If any reassignment takes place go , to 4th step else END

# Due to the K-Means initialization trap we have to use 'the' <i> K-Means++ </i>

## So we use the <i> Within cluster Sum of Squares </i>  and use the Elbow method to select optimal number of cluster

[ to know abut the <- operator I used in R ](https://www.statmethods.net/management/operators.html)

![down](https://upload.wikimedia.org/wikipedia/commons/e/ea/K-means_convergence.gif)

# It is a Interative process
