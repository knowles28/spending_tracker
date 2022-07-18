class Merchant:
    def __init__(self, name, restricted=False, _id=None):
        self.name = name
        self.restricted = restricted
        self.id = _id