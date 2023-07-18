import json


def create_file(file_name, content=None):
    # """Crea archivos sin contenido"""
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error
    if content and isinstance(content, (list, dict)):
        json_file = json.dumps(content)
        file.write(content)
    file.close()


def modify_file(file_name, content, overwrite=False):
    # """modifica el archivo file name
    # si overwrite es true sobreescribira el archivo"""
    if not isinstance(content, dict| list) or content == "":
        raise ValueError("'content' argument must be specified")

    file = open(file_name)
    file_content=json.loads(file.read())
    file.close
    if isinstance(file_content,list):
        if isinstance(content,dict):
            file_content.append(content)
        elif isinstance(content,list):
            file_content+=content
    if isinstance(file_content,dict):
        if isinstance(content, dict):
            file_content = [file_content, content]

        elif isinstance(content, list):
            file_content = [file_content] + content

    file= open(file_name,"w")
    file.write(json.dumps(file_content))
    file.close()


def reed_file(file_name):
    # """lee el contenido de un archivo"""
    file = open(file_name)
    contend = file.read()
    print(contend)
    file.close()

