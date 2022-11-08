from .strategyContract import Strategy
from core.data.waybill import DefaultWaybill

class SmsaStrategy(Strategy):
    creds = {
        'passkey': 'key1234'
    }

    def create_waybill(self, data: DefaultWaybill) -> str:
        return "smsa create_waybill response"

    def print_waybill(self, data: str):
        return 

    def track_shipment(self, data: str):
        return
