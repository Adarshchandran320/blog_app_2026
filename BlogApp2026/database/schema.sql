CREATE DATABASE IF NOT EXISTS blog_app_2026;
USE blog_app_2026;

CREATE TABLE users(
    user_id varchar(50) PRIMARY KEY,
    password varchar(255) NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL
);

CREATE TABLE blogposts(
    blog_id INT PRIMARY KEY,AUTO_INCREMENT,
    auth_id varchar(50) NOT NULL,
    title varchar(200) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(auth_id) REFERENCES users(user_id)
    ON DELETE CASCADE
);