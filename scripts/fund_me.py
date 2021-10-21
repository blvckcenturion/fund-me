from brownie import FundMe
from scripts.utils import get_account


def fund():
    print(FundMe)
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print(f"Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
