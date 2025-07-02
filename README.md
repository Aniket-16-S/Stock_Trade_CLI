# Stock Trading CLI Tool

## What is Stock Trading CLI Tool?

**Stock Trading CLI Tool** is a lightweight, modular command-line interface (CLI) application designed to place and manage equity and derivatives orders via [Dhan's API](https://dhan.co). This project simulates a microservice-like architecture and supports multiple order types such as market, limit, stop-loss, intraday, and F&O, with built-in logging and secure token handling.

This tool is designed for developers and traders who want a programmable interface to interact with their Dhan account for basic trading operations.

---

## Features

- Simple CLI-based interface for order placement and management.
- Supports **Market**, **Limit**, **Stop Loss**, **SL-M**, **IOC**, **CNC**, **Intraday**, **Futures**, and **Options** order types.

- Easy to set up—just add your Dhan credentials to get started.
- Lightweight and dependency-minimal.

---
## Structure 
```bash 
dhan-trading-cli/
|
├── input_handler.py     # Takes and validates user inputs
├── config.py            # Loads and manages credentials securely
├── dhan_trader.py       # Core logic for Dhan API communication
├── main.py              # CLI launcher and user authentication
├── logger.py            # Logs placed orders to CSV
├── requirements.txt     # Python package dependencies
└── .env                 # stores ClientID and Token (excluded from version control - User Specific )
```

---

## Requirements

- A valid [Dhan Trading Account](https://login.dhan.co/?location=DH_WEB&refer=DHAN_WEBSITE)
- Generate your **Client ID** and **Access Token** from the **APIs** section in your Dhan dashboard.

---

## Installation & Setup


1. **Clone the repository**  
```bash
git clone https://github.com/Aniket-16-S/Stock_Trade_CLI.git

```

```bash
cd Stock_Trade_CLI
```

2. **Install the required packages**  
```bash
pip install -r requirements.txt
```


3. **Create `.env` file**  
In the project root dir ( `Stock_Trade_CLI` ) , create a `.env` file and add:

```bash
DHAN_CLIENT_ID=your_client_id_here
DHAN_ACCESS_TOKEN=your_access_token_here
```


4. **Run the application**  
```bash
python main.py
```

The tool will place the order via Dhan API and log successful transactions in a CSV file (`order_log.csv`).


---

## Terms of Use

- This tool uses [Dhan’s  API](https://dhanhq.co/algo-trading/) in accordance with their terms and conditions.
- By using this CLI, you agree to [Dhan’s Terms & Conditions](https://dhan.co) and their [security](https://dhan.co/safety-security/) requirements .
- This project is intended for **educational and demonstrational purposes** only.
- **The developer is not responsible for any financial loss, API issues, or damage arising from use of this tool.**
- Always use caution when placing real trades—validate all inputs carefully.

---

## Notes & Recommendations

- Use this tool with your **main account credentials**, not sandbox/partner accounts.
- Never commit your `.env` file to any version control system.
- You can extend this project to support:
  - GTT orders
  - Portfolio performance tracking
  - Telegram/email alerts
  - Strategy-based bulk orders

---

## Future Goals

- Add support to fetch live market price (LTP).
- Integrate a user-friendly GUI.
- Implement better error handling and retry logic.
- Include additional analytics (PnL reports, portfolio breakdown, etc.).

## License

This project is under internal evaluation as part of an internship program and does not currently use an open-source license.
---