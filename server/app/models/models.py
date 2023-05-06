from pydantic import BaseModel
from typing import Union


class AppDetails(BaseModel):
    appname: str
    version: str
    email: str
    author: str


class GetStocksResponse(BaseModel):
    data: Union[list[dict], None] = None
