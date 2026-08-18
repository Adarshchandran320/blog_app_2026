class Menu:
    @staticmethod
    def welcome():
        print("\n--- Blog App ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    @staticmethod
    def logged_in_menu(user):
        print(f"\n--- Welcome, {user.full_name} ---")
        print("1. Create post")
        print("2. List posts")
        print("3. Update post")
        print("4. Delete post")
        print("5. Logout")