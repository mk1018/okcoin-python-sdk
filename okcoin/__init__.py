import asyncio
import okcoin.websocket as ws
from okcoin.utils.contains import WS_URL


class OkCoin:
    def __init__(
        self, api_key: str = None, secret_key: str = None, passphrase: str = None
    ):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

        self.loop = asyncio.get_event_loop()

    def execute_with_login(self, channels: list[str]):
        self.loop.run_until_complete(
            ws.subscribe(
                WS_URL, self.api_key, self.passphrase, self.secret_key, channels
            )
        )
        self.loop.close()

    def execute(self, channels: list[str]):
        self.loop.run_until_complete(ws.subscribe_without_login(WS_URL, channels))
        self.loop.close()
