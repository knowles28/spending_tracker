class Transaction:
    def __init__(self, _merchant_id, _description, _tag_id, _price, _date, _id=None):
        self.merchant_id = _merchant_id
        self.description = _description
        self.tag_id = _tag_id
        self.price = _price
        self._date = _date
        self.id = _id