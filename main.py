import config
from input_handler import get_order_inputs
from dhan_trader import DhanTrader
from order_logger import log_order_to_csv

def main():
    """
    Main function to run the Dhan trading application.
    """
    try:
        # 1. Authenticate: Initialize the trader with credentials from config
        trader = DhanTrader(client_id=config.CLIENT_ID, access_token=config.ACCESS_TOKEN)
        
        if not trader.dhan:
            print("Exiting application due to authentication failure.")
            return

        while True:
            # 2. Input: Get order details from the user
            order_details = get_order_inputs()

            # 3. Place Order: Send the order to the Dhan API
            api_response = trader.place_order(order_details)

            # 4. Show Result: Display the outcome to the user
            print("\n--- Order Response ---")
            if api_response and api_response.get('status') == 'success':
                order_id = api_response.get('orderId', 'N/A')
                print(f"   Order placed successfully!")
                print(f"   Order ID: {order_id}")
            else:
                reason = api_response.get('reason', 'No reason provided.')
                print(f"   Order placement failed. Reason: {reason}")
            # for debug :
            print(f"\nDebug : API RESPONCE \n{api_response}")


            # 5. Log to CSV: Save the transaction record
            log_order_to_csv(order_details, api_response)

            # Ask user if they want to place another order
            another = input("\nDo you want to place another order? (yes/no): ").strip().lower()
            if another != 'yes' or another != 'y':
                break
        
        print("\nThank you for using the Dhan Trading App!")

    except ValueError as ve:
        print(f"\nConfiguration Error in main : {ve}")
    except Exception as e:
        print(f"\nAn unexpected error occurred in main: {e}")


if __name__ == "__main__":
    main()