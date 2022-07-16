class Transaction:
    def __init__(self, _merchant, _description, _tag, _price, _date, _id=None):
        self.merchant = _merchant
        self.description = _description
        self.tag = _tag
        self.price = _price
        self.date = _date
        self.id = _id