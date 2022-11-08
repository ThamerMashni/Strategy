from .strategyContract import Strategy
from core.data.waybill import DefaultWaybill 
from core.data.taskDetails import TaskDetails 
class Courier():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    def create_waybill(self,data:DefaultWaybill) -> str:
        result = self._strategy.create_waybill(data=data)
        return(result)

    def print_waybill(self,awbNo:str) -> None:
        result = self._strategy.print_waybill(awbNo)
        return(result)

    def track_shipment(self, awbNo:str) -> TaskDetails:
        result = self._strategy.track_shipment(awbNo)
        return(result)

