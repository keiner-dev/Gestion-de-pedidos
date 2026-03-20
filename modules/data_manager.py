# modules/data_manager.py
import json
import os

CUSTOMERS_FILE = 'customers.json'
PRODUCTS_FILE = 'products.json'
ORDERS_FILE = 'orders.json'

def load_data(file_path):
    """
    Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file, or an empty dictionary if the file doesn't exist or is empty.
    """
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(file_path, data):
    """
    Saves data to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to save.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_customers():
    """Loads customer data."""
    return load_data(CUSTOMERS_FILE)

def save_customers(customers):
    """Saves customer data."""
    save_data(CUSTOMERS_FILE, customers)

def load_products():
    """Loads product data."""
    # Products are stored as tuples, but JSON stores them as lists.
    # We need to convert them back to tuples after loading.
    products_data = load_data(PRODUCTS_FILE)
    return {product_id: tuple(product_info) for product_id, product_info in products_data.items()}

def save_products(products):
    """Saves product data."""
    save_data(PRODUCTS_FILE, products)

def load_orders():
    """Loads order data."""
    return load_data(ORDERS_FILE)

def save_orders(orders):
    """Saves order data."""
    save_data(ORDERS_FILE, orders)
