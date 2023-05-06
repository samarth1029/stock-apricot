import pandas as pd
import uuid


def process_df(df, data) -> dict:
    df = df.drop(['Adj Close'], axis=1)
    df = df.drop(['Volume'], axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df['high_diff'] = (df.High.diff() / df.High * 100).round(2)
    df.iat[0, 6] = 0
    df['id'] = str(uuid.uuid1())
    create_dict_list_for_each_ticker(df, data)
    return df


def create_dict_list_for_each_ticker(df, data) -> list:
    for _item in df.index:
        _dict = {
            "id": df["id"][_item],
            "date": df["Date"][_item],
            "ticker": df["ticker_symbol"][_item],
            "high": round(float(df["High"][_item]), 2),
            "low": round(float(df["Low"][_item]), 2),
            "high_diff": round(float(df["high_diff"][_item]), 2)
        }
        data.append(_dict)
    return data
