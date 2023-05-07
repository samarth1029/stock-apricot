"""
main code for FastAPI setup
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from client.stock_apricot_app.server.app.api.api import Api
from client.stock_apricot_app.server.app.models.models import AppDetails
from client.stock_apricot_app.server.app.models.models import GetStocksResponse

description = """
API for collecting historic stock data for certain ticker symbols🚀

## 
* `get_top_gainers`: Get top 10 stocks whose price increased as compared to the previous day
* `get_top_losers`: Get top 10 stocks whose price decreased as compared to the previous day
* `generate_weekly_report`: Get weekly high, low and average for tickers

"""

tags_metadata = [
    {
        "name": "default",
        "description": "endpoints for details of app",
    },
    {
        "name": "stock-metrics",
        "description": "get stock metrics for ticker symbols",
    },
]

app = FastAPI(
    title="Stock Metrics",
    description=description,
    version="0.1",
    docs_url="/docs",
)


@app.get(
    "/",
)
def root():
    return {
        "message": "stock-metrics using Fast API in Python. Go to <IP>:8000/docs for API-explorer.",
        "errors": None,
    }


@app.get("/appinfo/", tags=["default"])
def get_app_info() -> AppDetails:
    return AppDetails(**Api().get_app_details())


@app.post(
    "/get_top_gainers",
    status_code=200,
    tags=["stock-metrics"],
)
def get_top_gainers() -> GetStocksResponse:
    if _response := Api().get_top_gainers():
        return GetStocksResponse(
            data=_response.get("data")
        )
    else:
        raise HTTPException(status_code=400, detail="Error")


@app.post(
    "/get_top_losers",
    status_code=200,
    tags=["stock-metrics"],
)
def get_top_losers() -> GetStocksResponse:
    if _response := Api().get_top_losers():
        return GetStocksResponse(
            data=_response.get("data")
        )
    else:
        raise HTTPException(status_code=400, detail="Error")


@app.post(
    "/get_weekly_report",
    status_code=200,
    tags=["stock-metrics"],
)
def get_weekly_report() -> GetStocksResponse:
    if _response := Api().get_weekly_report():
        return GetStocksResponse(
            data=_response.get("data")
        )
    else:
        raise HTTPException(status_code=400, detail="Error")


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8080, reload=True, debug=True, workers=3)
