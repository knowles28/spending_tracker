class Transaction:
    def __init__(self, merchant_id, description, tag_id, price, id=None):
        self.merchant_id = merchant_id
        self.description = description
        self.tag_id = tag_id
        self.price = price
        self.id = id