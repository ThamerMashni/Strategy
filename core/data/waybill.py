from .person import Person
from .item import Item
import datetime

class DefaultWaybill:
    shipper: Person
    customer: Person
    items: list[Item]
    sentDate: datetime.datetime

    def __init__(self, shipper:Person, customer:Person,items:list[Item],sentDate:datetime.datetime):
        self.shipper = shipper
        self.customer = customer
        self.items = items
        self.sentDate = sentDate


