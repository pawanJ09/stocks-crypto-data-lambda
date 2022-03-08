import requests
from model.stockscode import StocksCodeModel
from schemas.stock import StocksCodeSchema
from globals import headers
import os

scs = StocksCodeSchema()
scs_many = StocksCodeSchema(many=True)


def handle_refresh():
    stock_codes = fetch_stock_codes()
    refresh_url = os.environ.get('REFRESH_ENDPOINT')
    for stock in stock_codes:
        url = refresh_url.format(stock['stock_name'])
        invoke_refresh(stock, url)


def fetch_stock_codes():
    stock_codes = []
    response = StocksCodeModel.fetch_all()
    if response is not None and response['Count'] > 0:
        stock_codes = scs_many.dump(StocksCodeModel.fetch_all()["Items"])
    return stock_codes


def invoke_refresh(stock, url):
    response = requests.post(url=url, headers=headers, data=None)
    print(url, response)
    if response.status_code != 200:
        print(response, response.text)
