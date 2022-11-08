from .strategyContract import Strategy
from ..data.waybill import DefaultWaybill 

class AramexStrategy(Strategy):
    def __init__(self): 
        self.creds = {
        'username': 'aramexuser',
        'password': "pass",
        'version' : '1.1',
        'accountNumber': 123,
        'accountEntity': 'entity',
        'accountCountryCode': "SAU",
        'source': 1
    }
     

    def create_waybill(self, data: DefaultWaybill) -> str:
        return "Aramex create_watbill response"

    def print_waybill(self, data: str):
        return 

    def track_shipment(self, data: str):
        return
