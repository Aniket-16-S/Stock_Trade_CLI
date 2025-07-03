import os
from dotenv import load_dotenv

# Load environment variables from a .env file and update variables if changes were made.
load_dotenv(override=True)

# Fetch DhanHQ credentials
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

# Validate credentials :
if not CLIENT_ID or not ACCESS_TOKEN:
    raise ValueError("Error: DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN must be set in the .env file.")
    
# CSV Log file :
LOG_FILE = 'order_log.csv'