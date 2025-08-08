# MAIN TO RUN THE ENTIRE E-COMMERCE SMART SEARCH WORKFLOW

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.product_pipeline import search_our_products
from src.product_loader import display_product_catalog


def run_interactive_search():
    print("\nWELCOME TO OUR PRODUCT E-COMMERCE SMART SEARCH!\n")
    display_product_catalog()
    print("\nTYPE YOUR QUERY TO SEARCH FOR PRODUCTS AND CLICK ENTER. EG: Show me running shoes under $100 with good reviews. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_query = input("YOUR QUERY: ").strip()
        if user_query.lower() in {"exit", "quit", "q"}:
            print("THANK YOU FOR VISITING OUR E-COMMERCE STORE, SEE YOU NEXT TIME!\n")
            break

        try:
            results = search_our_products(user_query)
            if results.empty:
                print("NO PRODUCTS MATCHEDD YOUR QUERY, TRY AGAIN...\n")
            else:
                print(f"THE TOP {len(results)} RESULTS:\n")
                for _, row in results.iterrows():
                    print(f"{row['product_name']} — ${row['price']:.2f}, {row['category']}, Rating: {row['rating']:.1f}, Score: {round(row.get('similarity_score', 0)*100,2)} %")
                    print(f"  {row['description']}\n")
        except Exception as e:
            print(f"ERROR DURING SEARCH: {e}\n")



if __name__ == "__main__":
    run_interactive_search()

