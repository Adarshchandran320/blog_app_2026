import mysql.connector
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from ui.menu import Menu
from utils.validators import validate_required,validate_user_id


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
    def create_post(self):
        print("\n---------create a post---------")
        title = input("Enter Title: ")
        valid, message = validate_required(title, "title")
        if not valid:
            print(message)
            return
        description=input("Enter Description: ")
        valid,message=validate_required(description,"Description")
        if not valid:
            print(message)
            return
        try:
            self.blog_service.create_post(
                self.current_user,title.strip(),
                description.strip()
            )
            print("Post created Successfully.")
        except mysql.connector.Error as e:
            print("Database operation failed",e)

    def list_posts(self):
        print("=====Recent Post=======")
        try:
            posts = self.blog_service.list_posts()
            if not posts:
                print("No post available")
                return
            for post in posts:
                print("\n------------")
                print("Blog ID: ", post["blog_id"])
                print("Author: ", post["author_name"])
                print("Title: ", post["title"])
                print("Description: ", post["description"])
                print("Posted: ", post["created_at"])
        except mysql.connector.Error as e:
            print("Database operation failed:", e)


    def update_post(self):
        print('\n------------UPDATE POST-----------')
        try:
            blog_id = int(input("Enter blog ID:"))
        except ValueError:
            print('Blog ID must be a number')
            return
        title = input('Enter new title:')
        valid, message = validate_required(title, "title")
        if not valid:
            print(message)
            return
        description = input("Enter new description:")
        valid, message = validate_required(description, "Description")
        if not valid:
            print(message)
            return
        try:
            updated = self.blog_service.update_post(
                self.current_user,
                blog_id,
                title.strip(),
                description.strip()
            )
            if updated:
                print('post updated successfully')
            else:
                print("Post not found or you are not the owner of this post")
        except mysql.connector.Error as e:
            print("DB operation failed:", e)

    def delete_post(self):
        print("-------Delete Post-------")
        try:
            blog_id = int(input("Enter the blog id:"))
        except ValueError:
            print("Blog id must be a number")
            return
        try:
            deleted = self.blog_service.delete_post(
                self.current_user,
                blog_id
            )
            if deleted:
                print("Post deleted successfully")
            else:
                print("Post not found or you are not the owner of this post")
        except mysql.connector.Error as e:
            print("DB operation failed:", e)

    def logout(self):
        self.current_user = None
        print("Logged out successfully")

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


if __name__ == "__main__":
    app = BlogApp()
    app.run()