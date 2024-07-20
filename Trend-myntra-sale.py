import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data 
myntra = pd.read_excel(r"sales.xlsx")
myntra.dropna(inplace=True) 
myntra.drop_duplicates()

features = ['Product Name', 'Product Brand']

def transform_input(series):
    return ' '.join(series).lower()

myntra['content'] = myntra[features].astype(str).apply(transform_input, axis=1)

# Vectorize text data
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(myntra['content'])

# Apply TF-IDF
tfidf_transformer = TfidfTransformer()
tfidf = tfidf_transformer.fit_transform(bow)

# Apply LSA or LSI
lsa = TruncatedSVD(n_components=100, algorithm='arpack')
lsa.fit(tfidf)

# Compute cosine similarity
item_index = 2000
similarity_scores = cosine_similarity(tfidf[item_index], tfidf)
similar_items = list(enumerate(similarity_scores[0]))
sorted_similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:6]

# Filter similar items
similar_indices = [i for i, score in sorted_similar_items]
similar_df = myntra.iloc[similar_indices].copy()  # Use .copy() to avoid SettingWithCopyWarning

# Preprocess numeric features for trend score calculation
scaler = MinMaxScaler()

# Clean and convert numeric columns
similar_df.loc[:, 'Product Price'] = similar_df['Product Price'].str.replace('Rs.', '').astype(float)
similar_df.loc[:, 'Discount'] = similar_df['Discount'].str.replace('% OFF', '').str.replace('Rs.', '').str.replace('OFF', '').astype(float)
similar_df.loc[:, 'Verified Buyers'] = similar_df['Verified Buyers'].str.replace('k', '000').astype(float)
similar_df.loc[:, ['Product Price', 'Discount', 'Product Rating', 'Verified Buyers']] = scaler.fit_transform(similar_df[['Product Price', 'Discount', 'Product Rating', 'Verified Buyers']])

# Calculate Trend Score
similar_df.loc[:, 'Trend Score'] = (similar_df['Product Rating'] * 0.6) + (similar_df['Verified Buyers'] * 0.2) + (similar_df['Discount'] * 0.1) + (similar_df['Product Price'] * 0.1)

# Sort products by Trend Score
trendy_similar_products = similar_df.sort_values(by='Trend Score', ascending=False)
print(trendy_similar_products.head(5))
# Print results
print("=== Item: ")
print("{}: {}".format(item_index, myntra['content'].iloc[item_index]))

print("=== Similar Items by Trend Score")
for i, row in trendy_similar_products.iterrows():
    print("{}: {}".format(i, row['content'])) 
    
