class AuditLog:
    def __init__(self, log_id, action, user_id, timestamp):
        self.log_id = log_id
        self.action = action
        self.user_id = user_id
        self.timestamp = timestamp
