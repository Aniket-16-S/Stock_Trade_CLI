from dhanhq import dhanhq
import datetime

class DhanTrader:
    def __init__(self, client_id, access_token):
        try:
            self.dhan = dhanhq(client_id, access_token)
            print("DhanHQ client authenticated successfully.")
        except Exception as e:
            print(f"Error authenticating with DhanHQ: {e}")
            self.dhan = None

    def _get_security_id(self, order_details: dict) -> str:
        """
        Finds the security_id for a given instrument based on user inputs.
        """
        symbol = order_details['symbol']
        exchange = order_details['exchange_segment']
        
        print(f"\nSearching for security ID for {symbol} in {exchange}...")

        # For Cash segments (NSE, BSE), the first result is usually the correct one.
        if exchange in ["NSE", "BSE"]:
            response = self.dhan.get_securities(exchange)
            for item in response['securities']:
                if item['symbol'] == symbol and exchange == 'NSE_EQ': # Example for NSE Equity
                    print(f"Found Security ID: {item['securityId']}")
                    return item['securityId']
            return None # If no match found

        # For Derivatives (NFO), we need to filter precisely.
        elif exchange == "NFO":
            instrument_type = order_details['instrument_type']
            expiry_date_str = order_details['expiry_date']
            expiry_date = datetime.datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
            
            # This API call fetches all derivatives for the symbol
            response = self.dhan.get_derivative_instruments(exchange, symbol)
            
            for instrument in response.get('derivativeInstruments', []):
                # Match instrument type
                if instrument.get('instrumentType') != instrument_type:
                    continue
                
                # Match expiry date
                inst_expiry = datetime.datetime.fromtimestamp(instrument.get('expiryDate')).date()
                if inst_expiry != expiry_date:
                    continue

                # If it's an option, also match strike and type
                if instrument_type == 'OPT':
                    strike = order_details['strike_price']
                    option_type = order_details['option_type']
                    if instrument.get('strikePrice') == strike and instrument.get('optionType') == option_type:
                        print(f"Found Security ID: {instrument['securityId']}")
                        return instrument['securityId']
                # If it's a future, we have a match
                elif instrument_type == 'FUT':
                    print(f"Found Security ID: {instrument['securityId']}")
                    return instrument['securityId']
        
        return None # Return None if no match is found

    def place_order(self, order_details):
        if not self.dhan:
            return {"status": "error", "reason": "DhanHQ client not initialized."}

        try:
            # 1. Get the Security ID first
            security_id = self._get_security_id(order_details)
            
            if not security_id:
                return {
                    "status": "error",
                    "reason": f"Could not find a unique instrument for the details provided: {order_details['symbol']}"
                }

            # 2. Place the order using the found security_id
            print(f"\nPlacing order for Security ID: {security_id}")
            
            response = self.dhan.place_order(
                security_id=security_id,  # CRITICAL CHANGE: Use security_id
                exchange_segment=order_details['exchange_segment'],
                transaction_type=order_details['transaction_type'],
                quantity=order_details['quantity'],
                order_type=order_details['order_type'],
                product_type=order_details['product_type'],
                price=order_details['price'],
                validity=order_details['validity'],
                tag='TradingApp' # Optional tag
            )
            return response

        except Exception as e:
            return {"status": "error", "reason": str(e)}