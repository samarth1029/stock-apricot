"""
log data from dataframe into sqlite database
"""
from sqlalchemy import create_engine
import pandas as pd


def log_into_db(data: list[dict]):
    engine = create_engine('sqlite:///weekStock.db', echo=True)
    df = pd.DataFrame(data).set_index('id')
    df.to_sql('weekly_stocks', engine, if_exists='replace')
