## E-COMMERCE PRODUCT CATALOG USING NLP (TF-IDF) SMART PRODUCT SEARCH

```
A small, self-contained project that demonstrates a local NLP smart search over an e-commerce product catalog using TF-IDF.
Everything runs locally, no external APIs required and code is split into modular src/*.py files so each responsibility is clear and testable.
```

### Project Goal:

This is tiny e-commerce product catalog with a natural-language search interface.

The search:

  1. Extracts the search constraints from user query such as user_query_price, user_query_rating, user_query_category.

  2. Filters the products using those constraints.

  3. Ranks matching products using a local TF-IDF vectorizer and the cosine similarity.

```
This repo is intentionally minimal and educational, ideal for prototyping, teaching, or extending into a production prototype (vector DB, embeddings, UI).
```


### Features:

    Load a small product catalog in JSON called PRODUCT_CATALOG.

    Create a searchable search_text field for each product (name + description + category + price (numeric tokens) + ratings (numeric tokens)).

    Developed a TF-IDF vectorizer and TFIDF_matrix (corpus matrix).

    Extract user constraints from natural language queries:

        a. price (under $100, $50, below 200)

        b. rating (4 stars, 4+, good, excellent)

        c. known category words

    Filter products by extracted constraints.

    Rank filtered products by cosine similarity (query vs. TF-IDF product vectors).

    Interactive CLI to query the catalog.


### Repository Structure

```bash
.
|   .gitignore             
|   README.md
|   requirements.txt
|   
+---data
|       product.py
|       __init__.py
|       
\---src
        experiment.ipynb
        main_product_search.py
        product_filter_by_extracted_user_query.py
        product_loader.py
        product_pipeline.py
        searchable_text.py
        user_query_extraction.py
        __init__.py
```

### Create a Virtual Environment
```bash
python -m venv name_your_venv

name_your_venv\scripts\activate
```

### Run the requirements.txt
```bash
pip install -r requirements.txt
```

### Sample Data

```bash
{"product_id": 100, "product_name": "Strider Shoes", "price": 80.27, "category": "Footwear",
     "description": "Lightweight running shoes with breathable mesh and cushioned sole.", "rating": 4.5},

    {"product_id": 101, "product_name": "TrailBlazer Boots", "price": 112.10, "category": "Footwear",
     "description": "Durable hiking boots with water-resistant and aggressive tread.", "rating": 4.6},

    {"product_id": 102, "product_name": "Comfy Sneakers", "price": 69.50, "category": "Footwear",
     "description": "Casual sneakers for daily wear with memory-foam insole.", "rating": 4.0},

    {"product_id": 103, "product_name": "AeroSport Shorts", "price": 34.88, "category": "Apparel",
     "description": "Moisture-wicking shorts with zip pocket for keeping items.", "rating": 4.7},

    {"product_id": 104, "product_name": "Pulse Wireless Headphones", "price": 189.88, "category": "Electronics",
     "description": "Noise-cancelling over-ear headphones with 72h battery life.", "rating": 4.5}
```

### Run the main

```bash
python main_product_search.py
```

#### Sample Queries

```bash
Show me running shoes under $100 with good reviews
cheap backpacks above $20 with excellent reviews
yoga mat with 4+ stars
noise cancelling headphones below $150
```

#### Sequence of Execution

```bash

Parse user_query_price, user_query_rating, and user_query_category from the user's query,

Apply filters to the product DataFrame,

Transform the query into TF-IDF using the vectorizer produced at startup,

Compute cosine similarity and display the top results with scores.
```

#### Implementation Notes

```bash
Why TF-IDF? This is a small catalog (≤ few thousands), TF-IDF plus cosine similarity is fast and interpretable. It matches on word overlap and term importance.

Numeric tokens: Adding price_89 / rating_4.5 to search_text is a simple trick that lets textual queries referencing numbers be partially handled by TF-IDF.

Heuristics: Qualitative words (good, excellent, top rated) map to numeric rating thresholds (e.g., good → 4.5). These are heuristics and subject to tuning.

Separation of concerns: Modules are kept narrow so unit tests are easy and swapping pieces (e.g., TF-IDF → embeddings) is straightforward.

Scaling: For larger catalogs, precompute vectors and move ranking into an ANN / vector DB (FAISS, Milvus etc).
```

#### Further Works:
```bash
Replace TF-IDF with OpenAI embeddings or local sentence embeddings (e.g., sentence-transformers) for semantic search.

Persist vectors to disk or a vector DB for faster startup.

Add a small web UI (Streamlit / Flask + React). A Streamlit version is quick to build and useful for demos.

Add product images, pagination, and an “Add to cart” mockup for a more realistic prototype.
```

#### Author:
```bash
Name: Olanrewaju Adegoke
Email: Larrysman2004@yahoo.com
```



