import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch DhanHQ credentials
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

# Validate that credentials are set
if not CLIENT_ID or not ACCESS_TOKEN:
    raise ValueError("Error: DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN must be set in the .env file.")

# CSV Log file configuration
LOG_FILE = 'order_log.csv'