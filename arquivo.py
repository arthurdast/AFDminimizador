def listarArquivo():
    arquivo = open('alfabeto2.txt', 'r')
    lista = arquivo.readlines() 
    arquivo.close()
    return lista

