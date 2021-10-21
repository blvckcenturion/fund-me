from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIROMENTS


def deploy_fund_me_contract():
    """
    Deploys the contract to the network
    """
    # Deploy the contract
    account = get_account()
    print(get_account())
    # Publish source + ENV variable ETHERSCAN_TOKEN will publish our contract code to EtherScan
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"FundMe deployed at {fund_me.address}")

    return fund_me


def main():
    """
    Deploys the contract to the network
    """
    deploy_fund_me_contract()
