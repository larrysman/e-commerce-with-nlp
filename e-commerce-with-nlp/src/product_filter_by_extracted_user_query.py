# PRODUCT FILTERING USING THE EXTRACTED USER QUERY DEFINED CONSTRAINTS


import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.searchable_text import develop_tfidfVectorizer_matrix
from typing import Optional
from sklearn.metrics.pairwise import cosine_similarity


# PRODUCT FILTERING

def apply_product_filter(user_price: Optional[float] = None,
                  user_rating: Optional[float] = None,
                  user_category: Optional[str] = None) -> pd.DataFrame:
    """
    Filter the DataFrame using:
    Args:
       - user price 
       - user rating 
       - user category
       If all is available hence None.
    Returns:
        Filtered DataFrame.
    """

    df, vectorizer, tfidf_matrix = develop_tfidfVectorizer_matrix()
    
    filtered_df = df.copy()

    if user_category:
        filtered_df = filtered_df[filtered_df['category'].str.lower().str.contains(user_category.lower(), na=False)]
    if user_price is not None:
        filtered_df = filtered_df[filtered_df['price'] <= user_price]
    if user_rating is not None:
        filtered_df = filtered_df[filtered_df['rating'] >= user_rating]
    return vectorizer, tfidf_matrix, filtered_df




# FILTERED PRODUCTS RANKED USING TF-IDF COSINE SIMILARITY

def vectorize_and_rank_query_sim_score(user_query: str, top_n: int = 2) -> pd.DataFrame:
    """
    Rank products in `filtered_df` by similarity to `user query`, using TF-IDF computed
    on the input df for search_text and the provided tfidf_matrix - rows correspond to full_df.index.

    Args:
        user_query

    Returns:
        pd.DataFrame of top_2 products with an added similarity_score column.
    """
    vectorizer, tfidf_matrix, filtered_df = apply_product_filter()

    if filtered_df.empty:
        return filtered_df.copy()

    # TRANSFORM THE USER QUERY WITH THE SAME VECTORIZER OBTAINED FROM TF-IDF MATRIX
    query_vec = vectorizer.transform([user_query])

    # TF-IDF MATRIX IS SLICED FOR ONLY FILTERED PRODUCTS ROWS
    idx = filtered_df.index.to_list()
    submatrix = tfidf_matrix[idx, :]

    # COSINE SIMILARITY BETWEEN USER QUERY VECTOR AND EACH PRODUCT VECTOR
    sims = cosine_similarity(query_vec, submatrix).flatten()

    # ATTACHED SIMILARITY SCORES AND SORT IN DESCENDING ORDER
    results = filtered_df.copy()
    results['similarity_score'] = sims
    results = results.sort_values('similarity_score', ascending=False).head(top_n)
    return results



if __name__ == "__main__":
    user_query = "Show me running shoes under $100 with good reviews"
    print(vectorize_and_rank_query_sim_score(user_query))