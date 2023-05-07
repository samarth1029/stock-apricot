from sqlalchemy import create_engine, text
from server.app.models.models import GetStocksResponse
from server.app.src.base.create_stock_df import create_df_and_log_into_db
from datetime import date, timedelta
from typing import Union


class StockDataOperation:
    def __init__(self, _query: str):
        self.query = _query
        self.response = GetStocksResponse()

    def execute(self) -> Union[list[dict]]:
        create_df_and_log_into_db(start_date=date.today() - timedelta(days=8), end_date=date.today())
        connection = self.establish_db_connection()
        query = connection.execute(text(self.query))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        # self.response.data = result.get("data")
        return result.get("data")

    @staticmethod
    def establish_db_connection():
        db_connect = create_engine('sqlite:///weekStock.db')
        return db_connect.connect()
