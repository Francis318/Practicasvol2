import json


def create_file(file_name, content=None):
    # """Crea archivos sin contenido"""
    mode = "w" if content else "x"
    try:
        file = open(f"{file_name}", mode)
    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error
    if content:
        if isinstance(content, (list, dict)):
            if isinstance(content, dict):
                data=[content]
            content = json.dumps(data,indent=2) 

        file.write(content)
    file.close()


def modify_file(file_name, content, overwrite=False):
    # """modifica el archivo file name
    # si overwrite es true sobreescribira el archivo"""
    if not isinstance(content, dict | list|str) or content == "":
        raise ValueError("'content' argument must be specified")

    file = open(f"{file_name}")
    file_content=file.read()
    try:
        file_content = json.loads(file_content)
    except Exception:
        file_content=file_content
    file.close()

    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)
        elif isinstance(content, list):
            file_content += content
    if isinstance(file_content, dict):
        if isinstance(content, dict):
            file_content = [file_content, content]

        elif isinstance(content, list):
            file_content = [file_content] + content

    file = open(f"{file_name}", "w")
    if not isinstance(file_content,str):
        file_content=json.dumps(file_content)
    file.write(file_content)
    file.close()

def reed_file(file_name):
    # """lee el contenido de un archivo"""
    file = open(f"{file_name}")
    content = file.read()
    file.close()
    try:
        return json.loads(content)
    except Exception:
        return content