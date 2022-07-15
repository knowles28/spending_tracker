class Transaction:
    def __init__(self, _description, _price, _date, _id=None):
        self.description = _description
        self.price = _price
        self.date = _date
        self.id = _id