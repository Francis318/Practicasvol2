import base_decoradores
import json

def file_log(func):
    def wrapper(*args,**kwargs):
        file_name="activity.log"
        content="User saved\n"
        func(*args,**kwargs)
        try:
            base_decoradores.reed_file(file_name)
            base_decoradores.modify_file(file_name, content)
        except FileNotFoundError:
            base_decoradores.create_file(file_name,content)
            
    return wrapper

def console_log(func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        func(*args,**kwargs)
        print(f"{instance.__class__} saved")
    return wrapper

def save_data(file_name,content):
    try:
        base_decoradores.reed_file(file_name)
        base_decoradores.modify_file(file_name, content)
    except FileNotFoundError:
        base_decoradores.create_file(file_name, content)
        return content

class User:
    Class_name="Usuario"
    def __init__(self, username, name, last_name, password):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.password = password

    @file_log
    @console_log
    def save(self):
        file_name = "Users.json"
        content = self.__dict__
        return save_data(file_name,content)

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
            base_decoradores.reed_file(file_name)
            base_decoradores.modify_file(file_name, contend)
        except FileNotFoundError:
            base_decoradores.create_file(file_name, contend)


class Comments:
    def __init__(self, content, created_by, article):
        self.content = content
        self.created_by = created_by
        self.article = article

    def save(self):
        file_name = "Comments"
        contend= self
        try:
            base_decoradores.reed_file(file_name)
            base_decoradores.modify_file(file_name, contend)
        except FileNotFoundError:
            base_decoradores.create_file(file_name, contend)
        


# Comments
comments1 = Comments("Hola", "Francisco", "1")
comments2 = Comments("Segundo contenido", "Kike", "2")
# User
user1 = User("Francis", "Francisco", "Reyes", "123")
user2 = User("Kike", "Enrique", "Alaniz", "456")
Main_users = [user1, user2]
# Article
article1 = Article("new post", "hola", "status1", "imagen.jpg")
article2 = Article("new picture", "ardilla comiendo", "status2", "ardilla.jpg")
Main_article = [article1, article2]

user1.save()
#User.save(user1)
#User.save(user2)
# Article.save(article1)
# Article.save(article2)
# Comments.save(comments1)
# Comments.save(comments2)
