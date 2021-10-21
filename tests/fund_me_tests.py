from brownie import network, accounts
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIROMENTS
from scripts.deploy import deploy_fund_me_contract
import pytest


def tests():
    account = get_account()
    fund_me = deploy_fund_me_contract()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("Only run on local blockchain")

    account = get_account()
    fund_me = deploy_fund_me_contract()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
