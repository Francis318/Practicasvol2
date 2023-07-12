def  create_file(file_name,content=None):
    #"""Crea archivos sin contenido"""
    mode="w" if content else "x"
    file= open(file_name,mode)
    if content:
        file.write(content)
    file.close()

create_file("sample1.txt","contenido de archivo")
create_file("sample2.txt",)

def modify_file(file_name,content,overwrite=False):
    #"""modifica el archivo file name
    # si overwrite es true sobreescribira el archivo"""
    mode="w" if overwrite else "a"
    file= open(file_name,mode)
    file.write(content)
    file.close

modify_file("sample1.txt","Este contenido fue sobreescrito",overwrite=True)
modify_file("sample2.txt","Este contenido fue adicionado")
def  reed_file(file_name):
    #"""lee el contenido de un archivo"""
    file= open(file_name)
    contend = file.read()
    print(contend)
    file.close()

reed_file("sample1.txt")
