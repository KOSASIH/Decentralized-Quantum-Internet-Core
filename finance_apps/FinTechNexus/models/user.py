class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.transactions = []
        self.budgets = []
