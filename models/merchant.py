class Merchant:
    def __init__(self, name, restricted=False, id=None):
        self.name = name
        self.restricted = restricted
        self.id = id
    
    def mark_restricted(merchant):
        merchant.restricted = True
        return merchant
    
    def mark_unrestricted(merchant):
        merchant.restricted = False
        return merchant