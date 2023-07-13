class User:
    user_id: int
    name: str
    partner_id: int

    def __init__(self, user_id, name=None, partner_id=None):
        self.user_id = user_id
        self.name = name
        self.partner_id = partner_id
