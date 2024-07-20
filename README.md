
# Project Objective

In this project, we investigate a custom-made dataset carrying real-time information about Myntra products. The main aim is to perform descriptive and statistical analysis based on several designed goals.

This project was originally part of a solution built for the Myntra HackerRamp (WeForShe 2024) organised during the month of June- July 2024 organised by online e-commerce platform Myntra . Our goal was to develop an AI-driven product recommendation system based on ongoing trends, featuring virtual try-ons backed by 3D avatars. The Google Drive link to the idea template of our project is given below: https://docs.google.com/presentation/d/1BQdgk34B7UQlnkdiYZdwi6Ey3RCFSzEn/edit?usp=drivesdk&ouid=116813785334611979156&rtpof=true&sd=true 



## Dataset

 The dataset provides information on various aspects of Myntra products, including product name, brand, price, discount, rating, and verified buyers.                                                                                          The whole dataset is divided into three sub-categories of dataset:  a. Men, b. Women, c. Kids. for detailed analysis and insights into each categories.  
The analysis covers several areas, such as the influence of price range on sales, the impact of discounts on sales, the correlation between product ratings and sales on the three sub-categories mentioned above. and the identification of the most popular brands and their products.  
Additionally, a comprehensive analysis has been performed on the whole dataset which includes a fashion product recommendation feature based on current trends using ML algorithm.                                                                                
The dataset is prepared by scraping fashion products from the Myntra website using Selenium and Beautiful Soup, Python and is updated until June 2024.



## Exploratory Data Analysis on the three sub-categories

Load the Raw Data:
-  Begin by loading the raw data into the environment.

Data Cleaning:
-  Use Python libraries such as NumPy, Pandas, Matplotlib, and Seaborn to perform data cleaning.
- Ensure the data is properly pre-processed to accurately represent the correct information.

Preprocessing Steps:
- Remove unnecessary columns that do not contribute to the analysis.
- Drop duplicate rows to maintain data integrity.
- Remove null values to ensure completeness and accuracy of the dataset.



## Aims and Objectives

The analysis aims to provide insights into the following areas:
- How different price ranges influence the number of verified buyers (sales).
- How different discount ranges influence the number of verified buyers(sales).
- How product ratings influence the number of verified buyers(sales) across different price ranges.
- The top 10 most popular products in terms of verified buyers(sales) across three sections.
- The most popular products overall among the three sections.

## Fashion product recommendation by using pre-trained ML model

- Libraries and Data Loading:
Imports necessary libraries (pandas, numpy, seaborn, sklearn).
Loads and preprocesses data from an Excel file (WOMEN.xlsx).                          
- Text Feature Preparation:
Combines 'Product Name' and 'Product Brand' columns into a single lowercase string in the 'content' column.  
- Vectorization and TF-IDF Transformation:
Uses CountVectorizer to convert text data into a bag-of-words model.
Applies TF-IDF transformation to the bag-of-words matrix.                                                                    
- Latent Semantic Analysis (LSA):
Performs Truncated Singular Value Decomposition (SVD) to reduce dimensionality of the TF-IDF matrix.

- Cosine Similarity Computation:
Computes cosine similarity between a selected item (item_index = 2000) and all other items in the dataset.
Identifies the top 5 similar items based on cosine similarity scores.
-  Filtering and Preprocessing of Similar Items:
Extracts similar items' indices and creates a new DataFrame (similar_df) with these items.
Cleans and scales numeric columns ('Product Price', 'Discount', 'Verified Buyers') for trend score calculation.
-  Trend Score Calculation:
Calculates a trend score for each similar item based on weighted factors: Product Rating (60%), Verified Buyers (20%), Discount (10%), and Product Price (10%).
- Sorting and Displaying Results:
Sorts the similar items by their trend score in descending order.
Prints the top 5 trendy similar products and their details.
