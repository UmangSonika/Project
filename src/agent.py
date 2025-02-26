import json
import os
from tools import search_products, estimate_shipping, apply_discount, compare_prices, get_return_policy

LOG_FILE = "logs/interactions.log"

def log_interaction(user_input, response):
    """Logs user queries and responses to interactions.log."""
    log_entry = {
        "User Query": user_input,
        "Agent Response": response
    }
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(log_entry, indent=2) + "\n\n")

def process_query(user_input):
    response = {}
    
    # Task A: Basic Item Search + Price Constraint
    if "find" in user_input and "under" in user_input:
        words = user_input.split()
        max_price = None
        for i, word in enumerate(words):
            if word == "under":
                try:
                    max_price = float(words[i+1].strip("$").replace(",", ""))
                    break
                except ValueError:
                    pass
        response["search_results"] = search_products(user_input, max_price=max_price) if max_price else []
    
    # Apply discount if applicable
    if "discount code" in user_input:
        words = user_input.split()
        code = words[-1]  # Assume last word is the discount code
        if response.get("search_results"):
            item_price = response["search_results"][0].get("price", 0)
            response["discounted_price"] = apply_discount(code, item_price)

    # Task B: Shipping Deadline
    if "arrive by" in user_input:
        response["shipping"] = estimate_shipping("User Location", "Requested Date")

    # Task C: Competitor Price Comparison
    if "better deals" in user_input:
        product_name = "Casual Denim Jacket"
        response["price_comparison"] = compare_prices(product_name)

    # Task D: Returns & Policies
    if "return" in user_input or "policy" in user_input:
        words = user_input.split()
        store_name = next((word for word in words if word.startswith("Site")), "Unknown")
        response["return_policy"] = get_return_policy(store_name)

    # Task E: Multi-tool Integration (Handling Multiple Requests in One Query)
    if any(x in user_input for x in ["find", "compare", "shipping", "return", "discount"]):
        response["multi_tool_results"] = {
            "search": response.get("search_results"),
            "shipping": response.get("shipping"),
            "discount": response.get("discounted_price"),
            "price_comparison": response.get("price_comparison"),
            "return_policy": response.get("return_policy"),
        }

    # Ensure logs directory exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_interaction(user_input, response)  # Log the interaction
    return json.dumps(response, indent=2)

if __name__ == "__main__":
    while True:
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        print(process_query(user_query))
