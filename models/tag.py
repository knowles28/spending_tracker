class Tag:
    def __init__(self, name, restricted=False, id=None):
        self.name = name
        self.restricted = restricted
        self.id = id
        
        
    def mark_restricted(tag):
        tag.restricted = True
        return tag
    
    def mark_unrestricted(tag):
        tag.restricted = False
        return tag