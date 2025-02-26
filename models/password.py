class Password:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'service': self.service,
            'username': self.username,
            'password': self.password
        }

    @staticmethod
    def from_dict(data):
        return Password(data['service'], data['username'], data['password'])