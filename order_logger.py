import csv
from datetime import datetime
import os
from config import LOG_FILE

def log_order_to_csv(order_details, api_response):
    """
    Logs the details of a placed order and its result to a CSV file.

    Args:
        order_details (dict): The dictionary of user-provided order inputs.
        api_response (dict): The response dictionary from <- main <- dhan_trader.
    """

    file_exists = os.path.isfile(LOG_FILE)
    
    # Extract status and order_id from the response
    
    status = api_response.get('status', 'error')
    order_id = api_response.get('orderId', 'N/A')
    
    if status == 'Failed':
        status = f"ERROR: {api_response.get('reason', 'Unknown')}"

    log_data = {
        "Timestamp"   : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Symbol"      : order_details.get('symbol', 'NoSymbolDetected'),
        "Quantity"    : order_details.get('quantity', 'NoQTYdetected'),
        "Order Type"  : order_details.get('order_type', 'OrdTypNotDetected'),
        "Price"       : order_details.get('price', 0) if order_details.get('price', 0) > 0 else "MARKET", 
        "Product Type": order_details.get('trade_type', 'TrdTypNotDetected'),
        "Exchange"    : order_details.get('exchange_segment', 'ExchgSegNotDetected'),
        "Order ID"    : order_id,
        "Status"      : status
    }
    
    headers = log_data.keys()

    try:
        with open(LOG_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            if not file_exists:
                writer.writeheader()  # Write header only if file is newly created when opened.
            writer.writerow(log_data)

        print(f"Order successfully logged to {LOG_FILE}")
    except Exception as e:
        print(f"Error: Could not write to log file {LOG_FILE}. Reason: {e}")
