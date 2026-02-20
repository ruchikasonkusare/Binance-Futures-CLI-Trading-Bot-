def validate_inputs(symbol,side,order_type,quantity,price,stop_price):
    if not symbol:
        raise ValueError("Symbol is required")
    
    if side not in ["BUY","SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    
    if order_type not in ["MARKET","LIMIT","STOP"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    
    if quantity<=0:
        raise ValueError("Quantity must be greator than 0")
    
    if order_type=="LIMIT" and not price:
        raise ValueError("LIMIT order requires price")
    
    if order_type=="STOP" and (not price or not stop_price):
        raise ValueError("Stop order require stop price and price.")
    