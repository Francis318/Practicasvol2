import base
import json

user = {"username": "Francis", "name": "Francisco", "last_name": "Reyes"}
user2 = {"username2": "Jenri", "name2": "Enrique", "last_name2": "Alaniz"}
user_list=[user, user2]
json_file=json.dumps(user_list)

# try:
#     base.create_file("sample.txt",user_list)
# except OSError as error:
#     print("No se pudo crear el archivo: ", error)
base.modify_file("sample.txt",user_list,overwrite=False)

