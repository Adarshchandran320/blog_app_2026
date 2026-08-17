import mysql.connector
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from ui.menu import Menu


class BlogApp:
    def __init__(self):
        self.auth_service = AuthService(UserRepository())
        self.blog_service = BlogService(BlogRepository())
        self.current_user = None

    def run(self):
        while True:
            if self.current_user is None:
                Menu.welcome()
                choice = input("enter your choice: ")
                if choice == "1":
                    self.login()   
                elif choice == "2":
                    self.register() 
                elif choice == "3":
                    print("good bye!")
                    break
                else:
                    print("invalid choice")
            else:
                self.logged_in_menu()

    def register(self):
        print("\n======register==========")
        user_id = input("enter the user id:")
        valid, message = validate_user_id(user_id)
        if not valid:
            print(message)
            return

        password = input("enter the password:")
        valid, message = validate_required(password, "password")
        if not valid:
            print(message)
            return

        first_name = input('enter first name :')
        valid, message = validate_required(first_name, "first name")
        if not valid:
            print(message)
            return

        last_name = input("enter the last name:")
        valid, message = validate_required(last_name, "last name")
        if not valid:
            print(message)
            return

        try:
            success, message = self.auth_service.register(
                user_id.strip(),
                password,
                first_name.strip(),
                last_name.strip()
            )
            print(message)
        except mysql.connector.Error as e:
            print("database operation failed:", e)

    def login(self):
        print("\n-------------login-------------")
        user_id = input("enter the user id :")
        password = input("enter the password:")
        
        if not user_id or not password:
            print("user id and password cannot be blank")
            return
            
        try:
            user = self.auth_service.login(user_id, password)
            if user:
                self.current_user = user
                print(f"login successful. welcome, {user.first_name}")
            else:
                print("invalid user id or password")
        except mysql.connector.Error as e:
            print("database operation failed: ", e)

    def logged_in_menu(self):
        Menu.logged_in_menu(self.current_user)
        choice = input("enter your choice :")

        if choice == "1":
            self.create_post()
        elif choice == "2":
            self.list_posts()
        elif choice == "3":
            self.update_post()
        elif choice == "4":
            self.delete_post()
        elif choice == "5":
            self.logout()
        else:
            print("invalid choice")