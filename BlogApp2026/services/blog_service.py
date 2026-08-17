class BlogService:
    def __init__(self, blog_repository):
        self.blog_repository = blog_repository

    def create_post(self, user, title, description):
        self.blog_repository.create_post(user.user_id, title, description)

    def list_posts(self):
        return self.blog_repository.get_recent_posts()

    def update_post(self, user, blog_id, title, description):
        return self.blog_repository.update_post(
            blog_id, user.user_id, title, description
        )

    def delete_post(self, user, blog_id):
        return self.blog_repository.delete_post(blog_id, user.user_id)