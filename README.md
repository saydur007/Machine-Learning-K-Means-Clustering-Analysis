Overview
This project focuses on clustering customer data from a marketing campaign using unsupervised machine learning techniques. The dataset contains information such as customer income, age, and spending habits. The goal is to group customers into clusters based on their income and expenditure, allowing businesses to better understand their customers and tailor their marketing strategies accordingly.

Dataset
The dataset used in this project is publicly available on Kaggle: Customer Personality Analysis Dataset

Features
Date of Birth: The birth date of the customer.
Income: The annual income of the customer.
Expenditure: Total spending on various products (calculated during analysis).
Objective
The main goal of this analysis is to cluster the data based on income and expenditure, which helps in identifying customer segments. This will assist businesses in creating personalized marketing campaigns.

Data Preprocessing
Expenditure Calculation: A new column was created that sums up the total expenditure on various products for each customer.
Outlier Removal: Extreme income values, such as incomes over 600,000, were considered outliers and removed to avoid skewing the results.
Data Scaling: The Income and Spent columns were scaled to normalize the data, making the clustering algorithm more effective.
Clustering Methodology
We applied the KMeans Clustering algorithm, which is an unsupervised machine learning method. Before applying the algorithm, an Elbow Plot was used to determine the optimal number of clusters.

Elbow Plot
From the elbow plot, the optimal number of clusters was determined to be 4.

Results
Clusters
After applying KMeans clustering, the data was divided into four distinct clusters:

Cluster 0 (Green): Low-income, low-spending customers.
Cluster 1 (Orange): High-income, high-spending customers.
Cluster 2 (Blue): Moderate-income, moderate-spending customers.
Cluster 3 (Purple/Pink): Moderate-to-high income and spending customers.
Scatter Plot
A scatter plot was created with Income on the X-axis and Spent on the Y-axis. The clusters show a clear diagonal trend, indicating that income and spending are positively correlated—as income increases, spending tends to increase.

Key Insights
Cluster 0 (Green): Low-income, low-spending customers. A few outliers in this cluster indicate customers with low income but high expenditure, possibly due to external financial support.
Cluster 1 (Orange): High-income, high-spending customers. They can be targeted with premium products and personalized offers.
Cluster 2 (Blue): Moderate-income, moderate-spending customers. These customers may respond well to mid-tier products or bundled deals.
Cluster 3 (Purple/Pink): Moderate-to-high income and spending customers. These customers may be transitioning into higher spending and could be encouraged through loyalty programs and promotions.
Business Implications
By analyzing the clusters, businesses can adjust their marketing and sales strategies:

Cluster 1 (High-income, high-spending): Focus on premium products and personalized offers.
Cluster 0 (Low-income, low-spending): Focus on budget-friendly options and discounts.
Clusters 2 & 3 (Middle segments): Promote mid-tier products and offer bundled deals or loyalty programs to encourage spending.
Conclusion
The KMeans clustering analysis of the customer data provided several actionable insights into customer segmentation. The relationship between income and spending is evident, with higher-income customers tending to spend more. These insights enable businesses to craft differentiated marketing strategies for each customer segment, ultimately helping to maximize engagement and revenue.
