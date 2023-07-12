def  reed_file(file_name):
    #"""lee el contenido de un archivo"""
    file= open(file_name)
    contend = file.read()
    print(contend)
    file.close()

reed_file("sample1.txt")


