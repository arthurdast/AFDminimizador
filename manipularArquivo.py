from arquivo import *

def manipularArquivo():
    listar = listarArquivo()

    alfabeto= listar.pop(0).splitlines()        
    alfabeto= [i.split(',') for i in alfabeto]
    alfabeto= alfabeto[0]
    alfabeto[0]=alfabeto[0][9:]    

    estados= listar.pop(0).splitlines()
    estados= [i.split(',') for i in estados]    
    estados= estados[0]
    estados[0]=estados[0][8:]  


    inicial= listar.pop(0).splitlines()
    inicial= [i.split(',') for i in inicial]
    inicial= inicial[0]
    inicial[0]=inicial[0][8:]  



    final= listar.pop(0).splitlines()
    final= [i.split(',') for i in final]
    final= final[0]
    final[0]=final[0][7:]  

    

    del listar[0] #remover transições a palavra

    transicoesTemp=[]
    for ele in listar:
        if ele.strip():
            transicoesTemp.append(ele.replace("\n", ""))
            
    transicoesTemp2=[]
    for ele in transicoesTemp:
        transicoesTemp2+= ele.split(',')   

    transicoes3 = list()
    splitSize = 3
    for i in range(0, len(transicoesTemp2), splitSize):
      transicoes3.append(transicoesTemp2[i:i+splitSize])


    transicoesTemp3=[]
    for ele in transicoes3:
        for i in ele:
            if 'q' in i:
                eleTemp = i[1:]
                i = eleTemp                  
            transicoesTemp3.append(int(i))
    
    transicoes = list()
    splitSize = 3
    for i in range(0, len(transicoesTemp3), splitSize):
      transicoes.append(transicoesTemp3[i:i+splitSize])
    
    qInicial=[]
    for i in inicial:    
        qInicial.append(int(i[1:]))
    
    
    qFinal=[]
    for i in final:    
        qFinal.append(int(i[1:]))

    qEstados=[]
    for i in estados:    
        qEstados.append(int(i[1:]))    

    
    alfabetoCompleto= []
    alfabetoCompleto.append(alfabeto)
    alfabetoCompleto.append(qEstados)
    alfabetoCompleto.append(qInicial)
    alfabetoCompleto.append(qFinal)
    alfabetoCompleto.append(transicoes)    
    return (alfabetoCompleto)

