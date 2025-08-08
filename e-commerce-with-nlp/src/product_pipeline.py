# COMPLETE END-TO-END PIPELINE FOR RUNNING E-COMMERCE PRODUCT CATALOG WITH NLP AI SERACH IMPLEMENTATION


import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.searchable_text import develop_tfidfVectorizer_matrix
from src.user_query_extraction import extract_user_price, extract_user_category, extract_user_rating
from src.product_filter_by_extracted_user_query import apply_product_filter, vectorize_and_rank_query_sim_score


# END-TO-END PIPELINE

def search_our_products(user_query: str) -> pd.DataFrame:
    """
    Complete end-to-end pipeline implementation
      1. User Query ExtractionExtract constraints from query
      2. Apply Filtering to products over the available DataFrame
      3. Rank the filtered results using TF-IDF.

    Args:
        user_query

    Returns:
        top_n ranked results (DataFrame with similarity score.
    """

    new_df, vectorizer, tfidf_matrix = develop_tfidfVectorizer_matrix()

    # USER QUERY EXTRACTION
    USER_QUERY_PRICE = extract_user_price(user_query)
    USER_QUERY_RATING = extract_user_rating(user_query)
    USER_QUERY_CATEGORY = extract_user_category(user_query, new_df["category"].unique().tolist())

    # PRODUCT FILTERING
    vectorizer, tfidf_matrix, filtered_df = apply_product_filter(
        user_price=USER_QUERY_PRICE,
        user_rating=USER_QUERY_RATING,
        user_category=USER_QUERY_CATEGORY
    )

    # RANK FILTERED PRODUCT
    result_df = vectorize_and_rank_query_sim_score(user_query=user_query)

    return result_df




if __name__ == "__main__":
    user_query = "Show me running shoes under $100 with good reviews"
    print(search_our_products(user_query))