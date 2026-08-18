class User:
    def __init__(self, user_id, password, first_name, last_name):
        self.user_id = user_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"