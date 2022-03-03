from marshmallow import Schema, fields, INCLUDE, post_load
from model.stockscode import StocksCodeModel


class StocksCodeSchema(Schema):
    class Meta:
        unknown = INCLUDE
    stock_id = fields.Int()
    stock_name = fields.Str()
    stock_code = fields.Str()

    @post_load
    def return_obj(self, data, **kwargs):
        return StocksCodeModel(**data)

