#inporting the database connection 
from db.connection import DatabaseConnection

class BlogRepository:
    def create_post(self,user_id,title,description):
        connection = None
        cursor =None
        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor()
            cursor.execute(
                """INSERT INTO blogposts(auth_id,title,description,create)
                VALUES(%s,%s,%s,NOW())"""
                (user_id,title,description)
            )
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    def get_recent_posts(self):
        connection =None
        cursor =None
        try:
            connection= DatabaseConnection.get_connection()
            cursor=connection.cursor(dictionary=True)
            cursor.execute(
                """SELECT * FROM b.blog_id,CONCAT(u.first_name,' ',u.last_name) AS author_name,b.title,b.description,b.created_at
                from blogposts b
                Inner JOIN users u ON b.auth_id=u.user_id
                ORDER BY b.created_at DESC"""
            )
            results=cursor.fetchall()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    def update_post(self,blog_id,user_id,title,description):
        connection=None
        cursor=None
        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor()
            cursor.execute(
                """ Upadate blogposts set title=%s,description=%s where blog_id=%s and auth_id=%s"""
                (title,description,blog_id,user_id)
            )
            connection.commit()
            return cursor.rowcount>0
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    def delete_pos(self,blog_id,user_id):
        connection=None
        cursor=None
        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor()
            cursor.excecute(
                """DELETE from blogposts where blog_id=%s and auth_id=%s"""
                (blog_id,user_id)

            )
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
                