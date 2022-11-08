from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict
from ..data import waybill
class Strategy(ABC):

    creds: Dict

    @abstractmethod
    def create_waybill(self, data: waybill):
        pass
    @abstractmethod
    def print_waybill(self, data: str):
        pass
    @abstractmethod
    def track_shipment(self, data: str):
        pass
