# PRODUCT CATALOG LOADER MODULE


import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from data import product


# ACCESS THE DATA CATALOG

PRODUCTS = product.PRODUCT_CATALOG

def load_product_catalog(products = None) -> pd.DataFrame:
    """
    Load the product catalog from the data folder into a pandas DataFrame.

    Args:
        Json for input data catalog

    Returns:
        pd.DataFrame with stable integer index.
    """

    if products is None:
        products = PRODUCTS
    df = pd.DataFrame(products)

    expected_columns = ["product_id", "product_name", "price", "category", "description", "rating"]
    for col in expected_columns:
        if col not in df.columns:
            df[col] = None
    
    df = df.reset_index(drop=True)

    return df


# DISPLAYING THE PRODUCT CATALOG

def display_product_catalog():
    """
    Display the product catalog in a readable tabular format on the console.

    """
    df = load_product_catalog()

    print("\n===================================================== THE PRODUCT CATALOG =====================================================\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    display_product_catalog()