def create_order_payload(symbol,side,order_type,quantity,price=None,stop_price=None):
    payload={
        "symbol":symbol.upper(),
        "side":side.upper(),
        "type":order_type.upper(),
        "quantity":quantity        
    }
    
    if order_type.upper() =='LIMIT':
        payload["price"]=price
        payload['timeInForce']="GTC"
        
    elif order_type.upper()=="STOP":
        payload["price"]=price
        payload["stopprice"]=stop_price
        payload['timeInForce']="GTC"
        
    return payload