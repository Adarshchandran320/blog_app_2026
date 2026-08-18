from models.user import User

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, user_id, password, first_name, last_name):
        if self.user_repository.user_exists(user_id):
            return False, "user_id already exists"

       
        new_user = User(user_id, password, first_name, last_name)
        
        
        self.user_repository.create_user(new_user)
        
        return True, "registration successful"

    def login(self, user_id, password):
        data = self.user_repository.find_user(user_id, password)
        if not data:
            return None
            
        
        return User(
            data['user_id'],
            data['password'],
            data['first_name'],
            data['last_name']
        )