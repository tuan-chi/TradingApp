class Sock:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def serialize(self):
        return {
            'symbol': self.symbol,
            'name': self.name
        }

    def from_json(self, _json):
        self.symbol = _json['symbol']
        self.name = _json['name']
