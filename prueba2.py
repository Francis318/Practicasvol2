import practica_class
import json

def decorator1(func):
    def wrapper(self):
        print("Inicio")
        func(self)
        print("Final")
    return wrapper

class User:
    def __init__(self, username, name, last_name, password):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.password = password
        self.dict = {}

    @decorator1
    def save(self):
        file_name = "Users"
        contend = self
        try:
            practica_class.reed_file(file_name)
            practica_class.modify_file(file_name, contend)
        except FileNotFoundError:
            practica_class.create_file(file_name, contend)


class Article:
    def __init__(self, title, content, status, image):
        self.title = title
        self.content = content
        self.status = status
        self.image = image

    def save(self):
        file_name = "Articles"
        contend = self
        try:
            practica_class.reed_file(file_name)
            practica_class.modify_file(file_name, contend)
        except FileNotFoundError:
            practica_class.create_file(file_name, contend)


class Comments:
    def __init__(self, content, created_by, article):
        self.content = content
        self.created_by = created_by
        self.article = article

    def save(self):
        file_name = "Comments"
        contend= self
        try:
            practica_class.reed_file(file_name)
            practica_class.modify_file(file_name, contend)
        except FileNotFoundError:
            practica_class.create_file(file_name, contend)
        


# Comments
comments1 = Comments("Hola", "Francisco", "1").__dict__
comments2 = Comments("Segundo contenido", "Kike", "2").__dict__
# User
user1 = User("Francis", "Francisco", "Reyes", "123").__dict__
user2 = User("Kike", "Enrique", "Alaniz", "456").__dict__
Main_users = [user1, user2]
# Article
article1 = Article("new post", "hola", "status1", "imagen.jpg").__dict__
article2 = Article("new picture", "ardilla comiendo", "status2", "ardilla.jpg").__dict__
Main_article = [article1, article2]

User.save(user1)
# User.save(user2)
# Article.save(article1)
# Article.save(article2)
# Comments.save(comments1)
# Comments.save(comments2)
