from server.app.src.base.yahoo_finance_api_fetcher import YahooAPI
from server.app.utils.process_df import process_df
from server.app.utils.db_logger import log_into_db
from datetime import date, timedelta
from sqlalchemy import create_engine, text
import json


def create_df_and_log_into_db(start_date: date, end_date: date):
    dh = YahooAPI()
    with open(r"C:\BI\Projects\stock-apricot\server\data\raw\ticker_symbols.txt", "r") as f:
        tickers = [(line.strip()).split() for line in f]
    data = []
    for ticker in tickers:
        try:
            df = dh.get_ticker_data(str(ticker[0]), start_date, end_date)
            df['ticker_symbol'] = str(ticker[0])
            process_df(df, data)
        except Exception as e:
            print(f"Error: {e}")
            continue
    log_into_db(data)


if __name__ == "__main__":
    create_df_and_log_into_db(start_date=date.today() - timedelta(days=8), end_date=date.today())
    db_connect = create_engine('sqlite:///weekStock.db')
    connection = db_connect.connect()
    _query = """
            SELECT * FROM weekly_stocks;
            """
    query = connection.execute(text(_query))
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    print(len(result.get("data")))
    result = json.dumps(result, indent=4, separators=(',', ': '))
