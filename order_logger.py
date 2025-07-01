import csv
from datetime import datetime
import os
from config import LOG_FILE

def log_order_to_csv(order_details, api_response):
    """
    Logs the details of a placed order and its result to a CSV file.

    Args:
        order_details (dict): The dictionary of user-provided order inputs.
        api_response (dict): The response dictionary from the DhanHQ API.
    """
    file_exists = os.path.isfile(LOG_FILE)
    
    # Extract status and order_id from the response
    status = api_response.get('status', 'error')
    order_id = api_response.get('orderId', 'N/A')
    if status == 'error':
        status = f"ERROR: {api_response.get('reason', 'Unknown')}"

    log_data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Symbol": order_details['symbol'],
        "Quantity": order_details['quantity'],
        "Order Type": order_details['order_type'],
        "Price": order_details['price'] if order_details['price'] > 0 else "MARKET",
        "Product Type": order_details['product_type'],
        "Exchange": order_details['exchange_segment'],
        "Order ID": order_id,
        "Status": status
    }
    
    headers = log_data.keys()

    try:
        with open(LOG_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            if not file_exists:
                writer.writeheader()  # Write header only if file is new
            writer.writerow(log_data)
        print(f"Order successfully logged to {LOG_FILE}")
    except IOError as e:
        print(f"Error: Could not write to log file {LOG_FILE}. Reason: {e}")