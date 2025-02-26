import random
from datetime import datetime, timedelta

# Mock function: E-Commerce Search Aggregator
def search_products(query, max_price=None, size=None):
    mock_products = [
        {"name": "Floral Skirt", "price": 35, "size": "S", "stock": True},
        {"name": "White Sneakers", "price": 65, "size": "8", "stock": True},
        {"name": "Casual Denim Jacket", "price": 80, "size": "M", "stock": False},
    ]
    results = [p for p in mock_products if p["price"] <= (max_price or float('inf')) and (size is None or p["size"] == size)]
    return results

# Mock function: Shipping Time Estimator
def estimate_shipping(destination, desired_date):
    shipping_cost = random.randint(5, 20)
    estimated_arrival = datetime.now() + timedelta(days=random.randint(2, 7))
    return {"cost": shipping_cost, "arrival_date": estimated_arrival.strftime("%Y-%m-%d")}

# Mock function: Discount Checker
def apply_discount(code, price):
    valid_codes = {"SAVE10": 0.10, "WELCOME15": 0.15}
    discount = valid_codes.get(code, 0)
    final_price = round(price * (1 - discount), 2)
    return {"final_price": final_price, "discount_applied": discount > 0}

# Mock function: Competitor Price Comparison
def compare_prices(product_name):
    competitors = {
        "Casual Denim Jacket": {"SiteA": 80, "SiteB": 75, "SiteC": 70},
        "White Sneakers": {"SiteA": 65, "SiteB": 60, "SiteC": 68},
    }
    return competitors.get(product_name, {})

# Mock function: Return Policy Checker
def get_return_policy(site):
    policies = {
        "SiteA": "30-day return with free shipping.",
        "SiteB": "15-day return, customer pays shipping.",
        "SiteC": "No returns allowed.",
    }
    return policies.get(site, "Policy not found.")

