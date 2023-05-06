from server.app.src.base.exchange_rate_operation import (
    ExchangeRateOperation,
)
from server.app import (
    __version__,
    __appname__,
    __email__,
    __author__,
)


class Api:
    @staticmethod
    def get_app_details() -> dict:
        return {
            "appname": __appname__,
            "version": __version__,
            "email": __email__,
            "author": __author__,
        }

    @staticmethod
    def get_top_gainers() -> dict:
        _gainers_response = ExchangeRateOperation().execute()

        _gainers_list = _gainers_response.processed_response.data.currency_rates

        return {"data": _gainers_list}

    @staticmethod
    def get_top_losers() -> dict:
        _losers_response = ExchangeRateOperation().execute()

        _losers_list = _losers_response.processed_response.data.currency_rates

        return {"data": _losers_list}
