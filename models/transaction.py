class Transaction:
    def __init__(self, merchant, description, tag, price, date, id=None):
        self.merchant = merchant
        self.description = description
        self.tag = tag
        self.price = price
        self.date = date
        self.id = id