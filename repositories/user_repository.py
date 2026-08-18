from db.connection import DatabaseConnection

class UserRepository:
    
    def user_exists(self, user_id):
        connection = None
        cursor = None
        try:
            # Added () to actually call the function
            connection = DatabaseConnection.get_connection() 
            cursor = connection.cursor()
            
            # Added the missing comma between the query string and the tuple
            cursor.execute(
                "SELECT user_id FROM users WHERE user_id=%s",
                (user_id,)
            )
            return cursor.fetchone() is not None
        finally:
            # Fixed indentation
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def create_user(self, user):
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            
            # Fixed typo: "INSER" -> "INSERT"
            query = """
                INSERT INTO users(user_id, password, first_name, last_name)
                VALUES(%s, %s, %s, %s)
            """
            cursor.execute(query, (user.user_id, user.password, user.first_name, user.last_name))
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def find_user(self, user_id, password):
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            
            # Note: For AuthService.login to work with dictionary keys (data['user_id']),
            # this cursor needs to return a dictionary. If your driver supports it 
            # (like mysql-connector-python), you can pass dictionary=True here.
            cursor = connection.cursor(dictionary=True) 
            
            # Added comma between query and tuple, and fixed table name "user" to "users"
            cursor.execute(
                """
                SELECT user_id, password, first_name, last_name 
                FROM users WHERE user_id=%s AND password=%s
                """,
                (user_id, password)
            )
            return cursor.fetchone()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()