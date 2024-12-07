import os
from okcoin import OkCoin
from okcoin.utils.channels import PUBLIC_FUNCTIONS


def main():
    okcoin = OkCoin(
        api_key=os.getenv("API_KEY"),
        secret_key=os.getenv("SECRET_KEY"),
        passphrase=os.getenv("PASSPHARASE"),
    )

    channels = [
        PUBLIC_FUNCTIONS.depth("BTC", "JPY"),
        PUBLIC_FUNCTIONS.ticker("BTC", "JPY"),
    ]
    okcoin.execute(channels)


if __name__ == "__main__":
    main()
