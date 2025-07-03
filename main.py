from Dhan_CLI.config import *
from Dhan_CLI.dhan_trader import *
from Dhan_CLI.input_handler import *
from Dhan_CLI.order_logger import *
import sys

def authenticate_user() :
    try:
        global trader # making trader accessiblr to all functions

        #  Initializing the trader with credentials from config
        trader = DhanTrader(client_id=CLIENT_ID, access_token=ACCESS_TOKEN)
        
        if not trader.tradehull :
            print("Exiting application due to authentication failure.")
            sys.exit()  
    except Exception as e :
        print(f"Error : {e}")



def start_order():
    """
    Main function to run the Dhan trading CLI.
    """
    try:

        while True:
            # Geting order details from the user
            order_details = get_order_inputs()

            # Sending the order to the Dhan API
            api_response = trader.place_order(order_details)
            status = trader.get_status(order_id=order_id)
            # Display the outcome to the user
            print("\n--- Order Response ---")
            if api_response and api_response.get('status') == 'success':
                order_id = api_response.get('orderId', 'N/A')
                print(f"   Order placed successfully!")
                print(f"   Order ID  : {order_id}")
                print(f"   Status    : {status}")
            else:
                reason = api_response.get('reason', 'No reason provided.')
                print(f"   Order placement failed. Reason: {reason}")
            
            # Save the transaction record in Log CSV
            log_order_to_csv(order_details, api_response)

            # Ask user if they want to place another order
            another = input("\nDo you want to place another order? (yes/no): ").strip().lower()
            if another != 'yes' or another != 'y':
                break

    except ValueError as ve:
        print(f"\nConfiguration Error in main : {ve}")
    except Exception as e:
        print(f"\nAn unexpected error occurred in main: {e}")

def show_options() :
    print("\n------- Select Operation : -------")
    print("\n1. Place new Oders\n2. Get Order details (requires : Order_ID) \n3. Show current Holdings\n4. Cancel Order (requires : Order_ID)\n5. Cancel ALL Orders\n6. Show Balance\n7. Exit")
    opt = None
    while True :
        try :
            opt = int(input("\n : "))
            if opt in range(1, 8) :
                break
            print("Enter Valid option for operation") # If number is not in correct range
        except Exception :
            print("Enter Valid option for operation") # if user sends characters instead of numbers
    return opt

if __name__ == "__main__":
     
    authenticate_user()

    

    while True :
        opration = show_options()
        if opration == 1 :
            start_order()
        
        elif opration == 2 :
            try :
                order_id = int(input("Enter Order_ID : "))
            except ValueError :
                print("Please ENter correct order id")
                continue
            # We may place logic to verify order id with log file but order can be placed from different systems so . . .
            print(trader.get_order_details(order_id=order_id))
        
        elif opration == 3 :
            print(trader.get_holds())
        
        elif opration == 4 :
            try :
                order_id = int(input("Enter Order_ID : "))
            except ValueError :
                print("Please ENter correct order id")
                continue
            print(trader.cancel_specific_order(order_id=order_id))
        elif opration == 5 :
            print(trader.cancel_orders())
        elif opration == 6 :
            trader.get_balance()
        else :
            break
    
    print("\n\n . . . Thank You for using Dhan CLI Tool . . . \n\n")