# CREATING SEARCHABLE TEXT FIELD, VECTORIZER AND TF-IDF_MATRIX

import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.product_loader import load_product_catalog
from typing import Optional, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy


# CREATING SEARCHABLE TEXT FIELD

def create_search_text(df: pd.DataFrame) -> pd.DataFrame:
    """
    This create a new column 'search_text' to the DataFrame.
    Concatenate product_name, category, description, price and rating tokens.

    The combined text is what TF-IDF will be built on.

    Args:
        pd.DataFrame

    Returns:
        pd.DataFrame
    """
    def make_text(row):
        parts = [
            str(row.get("product_name", "")),
            str(row.get("category", "")),
            str(row.get("description", ""))
        ]
        
        # APPEND PRICE AND RATINGS SUCH THAT A USER CAN STATE THE PRICE OR RATINGS DURING QUERY.
        parts.append(f"price_{float(row['price']):.2f}" if pd.notnull(row.get('price')) else "")
        parts.append(f"rating_{float(row['rating']):.1f}" if pd.notnull(row.get('rating')) else "")
        text = " ".join([part for part in parts if part])
        return text.lower()
    
    new_df = df.copy()
    new_df['search_text'] = new_df.apply(make_text, axis=1)
    
    return new_df



# TF-IDF VECTORIZER AND VECTOR MATRIX
def develop_tfidfVectorizer_matrix(max_features: Optional[int] = None) -> Tuple[TfidfVectorizer, 'scipy.sparse.csr_matrix']:
    """
    Build a TfidfVectorizer from the DataFrame using the search_text column - list of strings.

    Args:
        max_features: None - if provided limits vocabulary size. This is useful for small memory.

    Returns:
        pd.DataFrame (containing the new column - search_text), vectorizer, tfidf_matrix
    """

    df = load_product_catalog()
    new_df = create_search_text(df)


    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform(new_df["search_text"])

    return new_df, vectorizer, tfidf_matrix


if __name__ == "__main__":
    df = load_product_catalog()
    df = create_search_text(df)
    new_df, vectorizer, tfidf_matrix = develop_tfidfVectorizer_matrix()
    print(vectorizer)
    print(tfidf_matrix)
    print(new_df)