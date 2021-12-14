import csv
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def create(self, order_file):
        pass

    @abstractmethod
    def process(self) -> float:
        pass


class OrderPandas(Order):
    def create(self, order_file):
        self.df = pd.read_csv(order_file)

    def process(self) -> float:
        total_by_item = self.df.order_count * self.df.price
        total: float = total_by_item.sum()
        return total


class OrderNumpy(Order):
    def create(self, order_file):
        # with open(order_file, "r") as fp:
        #     if fp.seek == 0:
        #         self.l = fp.read().split(",")
        #     else:
        #         pass
        # print(self.l)
        self.df = pd.read_csv(order_file)

    def process(self) -> float:
        order_count = np.array(self.df.order_count)
        price = np.array(self.df.price)
        total_by_item = order_count * price
        total = np.sum(total_by_item)
        return total


class Authorization(ABC):
    @abstractmethod
    def sms_auth(self, sms_code):
        pass


class SMSAuth(Authorization):
    def sms_auth(self, sms_code):
        print(f"Validating {sms_code}")
        self.validate = True


class PaymentProcess(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class CreditPayment(PaymentProcess):
    def __init__(self, code) -> None:
        self.code = code
        self.validate = False

    def pay(self, order, authsms: SMSAuth):
        pass


class DebitPayment(PaymentProcess):
    def __init__(self, code) -> None:
        self.code = code
        self.validate = False

    def pay():
        pass


class PaypalPayment(PaymentProcess):
    def __init__(self, email) -> None:
        self.email = email
        self.validate = False

    def pay(self, order, authsms: SMSAuth):
        if not authsms.validate:
            raise Exception(f"Not validated...")
        total = order.process()
        return total


if __name__ == "__main__":
    order = OrderPandas()
    order_file = "items.csv"
    order.create(order_file)

    auth = SMSAuth()
    auth.sms_auth(123)

    payment = PaypalPayment("pritamchayan.ghsh@gmail.com")
    total = payment.pay(order, auth)

    print(f"Order is in process with total price: {total}")
