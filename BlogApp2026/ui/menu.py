class Menu:
    @staticmethod
    def welcome():
        print("\n---blog app----")
        print("1.login")
        print("2.Register")
        print("3.Exit")
    @staticmethod
    def logged_in_menu(user):
        print("\n---Welcome----,{user.full_name}------")
        print("1.Create post")
        print("2.List post")
        print("3.Update post")
        print("4.Delete post")
        print("5.Logout")