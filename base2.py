import json
def create_file(file_name: str, content: list | dict = None):
    # """Crea archivos json"""
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error
    if content:
        json_file=json.dumps(content)
        file.write(json_file)
    file.close()


def modify_file(file_name, content, overwrite=False):
    # """modifica el archivo file name
    # si overwrite es true sobreescribira el archivo"""
    json_file=json.dumps(content)
    if not isinstance(json_file, str) or json_file == "":
        raise ValueError("'content' argument must be specified")

    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    file.write(json_file)
    file.close()


def reed_file(file_name):
    # """lee el contenido de un archivo"""
    file = open(file_name)
    contend = file.read()
    print(contend)
    file.close()
