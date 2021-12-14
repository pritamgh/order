import pytest

from order_pay import OrderNumpy, SMSAuth, PaypalPayment


@pytest.fixture(scope="module")
def variables():
    pytest.order = OrderNumpy()
    pytest.auth = SMSAuth()
    pytest.payment = PaypalPayment("testpritam.ghosh@gmail.com")


def test_order_create(variables):
    order_file = "items.csv"
    pytest.order.create(order_file)


def test_smsauth(variables):
    pytest.auth.sms_auth(1234)


def test_payment(variables):
    total = pytest.payment.pay(pytest.order, pytest.auth)
    assert total == 4104.26
