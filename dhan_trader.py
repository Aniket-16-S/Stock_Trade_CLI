import Dhan_Tradehull as dhan_tradehull 

class DhanTrader:
    def __init__(self, client_id, access_token):
        try:
            #self.dhan = dhanhq(client_id, access_token)   test if not req as tradehull has built in fnc to make this obj.

            # Initialize Dhan_Tradehull with the dhanhq instance
            self.tradehull = dhan_tradehull.Tradehull(client_id, access_token)
            print("DhanHQ client authenticated successfully.")

            self.client_id = client_id
            self.access_token = access_token

        except Exception as e:
            print(f"Failed authenticating or initializing: {e}")
            self.tradehull = None # Ensure tradehull is also None if initialization fails

    def place_order(self, order_details):
        if not self.tradehull: # Check if tradehull is initialized
            return {
                    "status": "Failed", 
                    "reason": "Dhan_Tradehull client not initialized."
                    }

        try:
            print(f"\nPlacing order for {order_details['symbol']} on {order_details['exchange_segment']}")

            response = self.tradehull.order_placement(

                tradingsymbol   =  order_details['symbol'],
                
                exchange        =  order_details['exchange_segment'],
                
                quantity        =  order_details['quantity'],
                
                price           =  order_details.get('price', 0), # Using .get() with a default for optional parameters
                
                trigger_price   =  order_details.get('trigger_price', 0),
                
                order_type      =  order_details['order_type'],
                
                transaction_type    =  order_details['transaction_type'],
                
                trade_type          =  order_details['trade_type'], 
                
                disclosed_quantity  =  order_details.get('disclosed_quantity', 0),
                
                after_market_order  =  order_details.get('after_market_order', False),
                
                validity            =  order_details.get('validity', 'DAY'),
                
                amo_time            =  order_details.get('amo_time', 'OPEN'),
                
                bo_profit_value     =  order_details.get('bo_profit_value', None),
                
                bo_stop_loss_Value  =  order_details.get('bo_stop_loss_Value', None)
            )


            print(f"\nOrder placement response from Dhan_Tradehull: {response}")
            
            # Wraping the response to dic
            if response :
                return {
                        "status": "success",
                        "orderId": response
                        } 
            else :
                return {
                        "status": "Failed", 
                        "reason": response
                        } 

        except Exception as e:
            return {
                    "status": "Failed", 
                    "reason": str(e)
                    }
        
    def get_report(self) :
        # Returns shares report from porfolio in 2 dict s
        order_details, order_exe_price =  self.tradehull.order_report()
        print("Order Details : ")
        for k, v in  order_details.items() :
            print(f"{k} : {v}")
        print("Order exe price : ")
        for k, v in  order_exe_price.items() :
            print(f"{k} : {v}")
    
    def get_status(self, order_id) :
        # Order ID required param hence default value as none was not set
        responce = self.tradehull.get_order_status(orderid=order_id)
        
        data = responce.get('data', 'N/A')
        status = responce.get('status', 'Error')
        rem = responce.get('remarks', 'None') 

        data = data.get('data')
        # As responce is like {'status': 'failure', 'remarks': 'list index out of range', 'data': {'status': 'success', 'remarks': '', 'data': []}}
        # i.e. Dic inside Dic
        print(f"Status : {status} \nRemarks : {rem} \nData : {data}")
    
    def get_order_details(self, order_id) :
        # Order ID required param hence default value as none was not set
        responce = self.tradehull.get_order_detail(order_id==order_id)
        data = responce.get('data', 'N/A')
        status = responce.get('status', 'Error')
        rem = responce.get('remarks', 'None') 

        data = data.get('data')
        # As responce is like {'status': 'failure', 'remarks': 'list index out of range', 'data': {'status': 'success', 'remarks': '', 'data': []}}
        # i.e. Dic inside Dic
        print(f"Status : {status} \nRemarks : {rem} \nData : {data}")


    def get_holds(self) :
        # returns holdings of the day
        responce = self.tradehull.get_holdings()
        for k, v in responce.items() :
            print(f"{k} : {v}")
    
    def cancel_orders(self) :
        # cancels all orders of the dat
        print(self.get_holds())
        sure = input("\n Are you sure to cancel all above orders (y/n) : ")
        if sure.lower() == 'y' :
            responce = self.tradehull.cancel_all_orders()
            for k, v in responce.items() :
                print(f"{k} : {v}")

        
    def cancel_specific_order(self, order_id) :
        # Cancels specific order
        responce =   self.tradehull.cancel_order(OrderID=order_id)
        print(f"responce : {responce}")
        
    
    def get_balance(self) :
        amt = self.tradehull.get_balance()
        print(f"\n Client ID : {self.client_id} \n Balance : {amt}")
