from botocore.exceptions import ClientError
from database import resource

table = resource.Table('stocks-code-dd')


class StocksCodeModel:

    def __init__(self, stock_id, stock_name, stock_code):
        self.stock_id = stock_id
        self.stock_name = stock_name
        self.stock_code = stock_code

    def json(self):
        return {"id": self.stock_id, "name": self.stock_name, "code": self.stock_code}

    def __repr__(self):
        return f"StocksCodeModel(id={self.stock_id!r}, name={self.stock_name!r}, " \
               f"code={self.stock_code!r})"

    @classmethod
    def fetch_all(cls):
        # This can be expensive if huge dynamo db table data exists
        try:
            response = table.scan()
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
