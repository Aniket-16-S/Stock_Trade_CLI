def get_order_inputs():
    """
    Collects and validates all necessary order details from the user,
    including specific details for derivative instruments.
    """
    print("\n--- Place a New Trading Order ---")

    # --- Symbol & Exchange ---
    symbol = input("Enter Symbol (e.g., RELIANCE, NIFTY, BANKNIFTY): ").strip().upper()
    while True:
        segment = input("Enter Exchange Segment (NSE, BSE, NFO): ").strip().upper()
        if segment in {"NSE", "BSE", "NFO"}:
            break
        print("Invalid segment. Please choose from NSE, BSE, NFO.")

    # --- Derivative Specific Inputs (if NFO) ---
    instrument_type = None
    expiry_date = None
    strike_price = 0.0
    option_type = 'NONE'

    if segment == 'NFO':
        while True:
            instrument_type = input("Enter Instrument Type (FUT for Futures, OPT for Options): ").strip().upper()
            if instrument_type in {"FUT", "OPT"}:
                break
            print("Invalid instrument type. Please choose FUT or OPT.")

        expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ").strip()
        
        if instrument_type == 'OPT':
            while True:
                try:
                    strike_price = float(input("Enter Strike Price: ").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical strike price.")
            
            while True:
                option_type = input("Enter Option Type (CE for Call, PE for Put): ").strip().upper()
                if option_type in {"CE", "PE"}:
                    break
                print("Invalid option type. Please choose CE or PE.")

    # --- Common Order Details ---
    while True:
        side = input("Enter Order Side (BUY, SELL): ").strip().upper()
        if side in {"BUY", "SELL"}:
            break
        print("Invalid side. Please choose BUY or SELL.")

    while True:
        order_type = input("Enter Order Type (MARKET, LIMIT, SL, SL-M): ").strip().upper()
        if order_type in {"MARKET", "LIMIT", "SL", "SL-M"}:
            break
        print("Invalid order type. Please choose from MARKET, LIMIT, SL, SL-M.")

    while True:
        try:
            quantity = int(input("Enter Quantity: ").strip())
            if quantity > 0:
                break
            print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    price = 0.0
    if order_type in ["LIMIT", "SL", "SL-M"]:
        while True:
            try:
                price = float(input(f"Enter Price for {order_type} order: ").strip())
                if price > 0:
                    break
                print("Price must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")

    while True:
        product_type = input("Enter Product Type (INTRADAY, CNC, NRML): ").strip().upper()
        if product_type in {"INTRADAY", "CNC", "NRML"}:
            break
        print("Invalid product type. Please choose from INTRADAY, CNC, NRML.")

    while True:
        validity = input("Enter Order Validity (DAY, IOC): ").strip().upper()
        if validity in {"DAY", "IOC"}:
            break
        print("Invalid validity. Please choose DAY or IOC.")

    # Return a dictionary including new derivative fields
    return {
        "symbol": symbol,
        "exchange_segment": segment,
        "instrument_type": instrument_type,
        "expiry_date": expiry_date,
        "strike_price": strike_price,
        "option_type": option_type,
        "transaction_type": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
        "product_type": product_type,
        "validity": validity,
    }