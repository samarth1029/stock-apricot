from server.app.src.base.stock_operations import (
    StockDataOperation,
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
        _query = """
                    WITH temporaryTable(ticker,high_diff,date,img)
                    AS(SELECT ticker,high_diff,MAX(date),img 
                    FROM weekly_stocks GROUP BY ticker)
                    SELECT ticker,high_diff,img FROM temporaryTable
                    ORDER BY high_diff DESC LIMIT 10;
                """
        _top_gainers_response = StockDataOperation(_query=_query).execute()
        return {"data": _top_gainers_response}

    @staticmethod
    def get_top_losers() -> dict:
        _query = """
                    WITH temporaryTable(ticker,high_diff,date,img)
                    AS(SELECT ticker,high_diff,MAX(date),img 
                    FROM weekly_stocks GROUP BY ticker)
                    SELECT ticker,high_diff,img FROM temporaryTable
                    ORDER BY high_diff ASC LIMIT 10;
                """
        _top_losers_response = StockDataOperation(_query=_query).execute()
        return {"data": _top_losers_response}

    @staticmethod
    def get_weekly_report() -> dict:
        _query = """
                    WITH temporaryTable(ticker,average,high,low,img)
                    AS(SELECT ticker,ROUND(AVG(high),2) AS average,MAX(high),MIN(low) ,img
                    FROM weekly_stocks GROUP BY ticker)
                    SELECT ticker,high,low,average,img FROM temporaryTable; 
                """
        _weekly_metrics_response = StockDataOperation(_query=_query).execute()
        return {"data": _weekly_metrics_response}


if __name__ == "__main__":
    _obj = Api().get_weekly_report()
    print(_obj)
