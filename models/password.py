from utils.password_checker import Password_checker

class Password:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password
        self.pwned, self.times = Password_checker.check_password(password)

    def to_dict(self):
        return {
            'service': self.service,
            'username': self.username,
            'password': self.password,
            'pwned' : self.pwned,
            'times' : self.times
        }

    @staticmethod
    def from_dict(data):
        return Password(data['service'], data['username'], data['password'])