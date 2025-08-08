# VERY SIMPLE NLP EXTRACTION MODULE FOR USER'S PRICE, RATING AND CATEGORY

import re
from typing import Optional, List


# USER PRICE EXTRACTION FROM USER QUERY
def extract_user_price(user_query: str) -> Optional[float]:
    """
    Extract 'user's price' from the user's query.
    Search for phrases like "under $100", "below 100", "< $80".

    Args:
        user_query
    Returns:
        price (float) or None
    """
    query = user_query.lower()
    
    # COMMON PATTERNS: 'UNDER $100', 'BELOW 100', '<100', 'LESS THAN 100'
    matching_pattern = re.search(r'(?:under|below|less than|<)\s*\$?\s*([0-9]+(?:\.[0-9]+)?)', query)
    if matching_pattern:
        return float(matching_pattern.group(1))
    
    # ABSOLUTE PREFERENCE: $NUMBER
    matching_pattern2 = re.search(r'\$\s*([0-9]+(?:\.[0-9]+)?)', query)
    if matching_pattern2:
        return float(matching_pattern2.group(1))
    return None



# USER RATING EXTRACTION FROM USER QUERY
def extract_user_rating(user_query: str) -> Optional[float]:
    """
    Extract user rating from the user's query.
    Recognizes rating phrases like '4 stars', '4+', 'good reviews' (mapped to 4.5), 'excellent' (5.0).
    
    Args:
        user_query
    Returns:
        rating (float) or None
    """
    query = user_query.lower()
    
    match_pattern = re.search(r'([0-5](?:\.[05])?)\s*[-+]?\s*stars?', query)
    if match_pattern:
        try:
            return float(match_pattern.group(1))
        except:
            pass
    
    match_pattern2 = re.search(r'([0-5])\s*\+\s*', query)
    if match_pattern2:
        return float(match_pattern2.group(1))
    
    # INCASE USER USES A QUALITATIVE DESCRIPTIONS - HEURISTIC WORDS
    if "excellent" in query or "best" in query or "top-rated" in query or "top rated" in query:
        return 5.0
    if "good reviews" in query or "good review" in query or "good" in query:
        return 4.5
    return None


# USER CATEGORY EXTRACTION FROM USER QUERY
def extract_user_category(user_query: str, categories: List[str]) -> Optional[str]:
    """
    Search for any known category names in the user query.
    categories: list of valid category strings (e.g., ['Footwear','Apparel'])
    
    Args:
        user_query
        categories
    Returns:
        matched category or None
    """
    query = user_query.lower()
    for cat in categories:
        if cat.lower() in query:
            return cat
    return None




if __name__ == "__main__":
    user_query = "Show me running shoes from Apparel under $100 with good reviews."
    print(extract_user_price(user_query))
    print(extract_user_rating(user_query))
    print(extract_user_category(user_query, ["Footwear", "Apparel"]))