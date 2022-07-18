class Merchant:
    def __init__(self, name, restricted=False, id=None):
        self.name = name
        self.restricted = restricted
        self.id = id