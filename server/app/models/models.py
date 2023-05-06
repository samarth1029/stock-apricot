from pydantic import BaseModel
from typing import Union, List


class AppDetails(BaseModel):
    appname: str
    version: str
    email: str
    author: str


class GetStocksResponse(BaseModel):
    stock_data: Union[list[dict], None] = None
