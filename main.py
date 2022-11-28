import numpy as np
from manipularArquivo import *
from removerRepetidos import *


arquivo=manipularArquivo()
alfabeto = arquivo[0]
estados = arquivo[1]
inicial = arquivo[2]
final = arquivo[3]
transicoes = arquivo[4]


matrizTamanho = len(estados)
matriz = np.full((matrizTamanho,matrizTamanho), 0)
print(matriz,"\n")   


                
for idx,x in enumerate(matriz, start=0):
        for idy,y in enumerate(matriz, start=0):                 
            for q in final:   
                if( q == idx) and (q != idy):                        
                    matriz[idy][idx]= 1
                if(q == idy) and (q != idx):                                                
                    matriz[idy][idx]= 1                
            if idx in final:                    
                if idy in final:   
                   matriz[idy][idx]= 0   

print(matriz,"\n")                                                         
tempA=0
tempB=0
for idx,x in enumerate(matriz, start=0):
        for idy,y in enumerate(matriz, start=0):    
            if(matriz[idx][idy] == 0):                
                for t in transicoes:
                    if(t[0] == idx  and t[2] == 0):
                        tempA = t[1]                        
                    if(t[0] == idy  and t[2] == 0):
                        tempB = t[1]                  
                for t in transicoes:
                    if(t[0] == idx  and t[2] == 1):
                        tempA = t[1]                        
                    if(t[0] == idy  and t[2] == 1):
                        tempB = t[1]                
                if(matriz[tempA][tempB] == 1):
                    matriz[idx][idy]=1
                
print(matriz,"\n")                    


matrizDiag = np.tri(matrizTamanho,matrizTamanho)

for idx,x in enumerate(matrizDiag, start=0):
        for idy,y in enumerate(matrizDiag, start=0):  
            if(matrizDiag[idx][idy] == 0): 
                matriz[idx][idy] = 999 
            if(idx == idy): 
                matriz[idx][idy] = 999     
                
print(matriz,"\n")       

listJuntar = []
for idx,x in enumerate(matriz, start=0):
        for idy,y in enumerate(matriz, start=0):  
            if(matriz[idx][idy] == 0):
                listJuntar.append([idy,idx]) 

print (listJuntar,"\n")             

estadosQ = []
estadosQfinal = []
for q in estados:
    for x in listJuntar:        
        if(x[0] == q or x[1] == q):                        
            estadosQ.append(x[0])
            estadosQ.append(x[1])
            for x in listJuntar:        
                if(x[0] == q or x[1] == q):                                
                    estadosQ.append(x[0])
                    estadosQ.append(x[1])
    estadosQt = remove_repetidos(estadosQ)        
    if not (estadosQt == []):
        estadosQfinal.append(estadosQt)
    else:
        estadosQfinal.append([q])
    estadosQ.clear()
                       
estadosQfinal = remove_repetidos(estadosQfinal)                                                       
print (estadosQfinal,"\n")    

transicoesQ = []
transicoesQfinal = [[]]
nEstado=0
novoEstados=[]
estadosFinais=[]
estadoInicialNovo=[]
for e in estadosQfinal:
    for ee in e:
        for t in transicoes:
            if (ee == t[0]):
                transicoesQ.append(t)
        novoEstados.append(nEstado)
    for t in transicoesQ:
        for idd,tDelete in enumerate(transicoesQ, start=0):
            if(t != tDelete):
                if(t[2] == tDelete[2]):
                    transicoesQ.pop(idd)    
    for es in e:
        if es in final:
            estadosFinais.append(nEstado)
    for ef in e:
        if ef in inicial:
            estadoInicialNovo.append(nEstado)                        
    qe= ['q'+str(i) for i in e]                        
    nEstado += 1         
    print (nEstado,"° estado. Junção do(s) estado(s) ",qe)
    
    print(transicoesQ,"\n")        
    if not (transicoesQ == []):
        transicoesQfinal.append([transicoesQ[0],transicoesQ[1]])
    transicoesQ.clear()
if transicoesQfinal[0]== []:
    transicoesQfinal.pop(0)
    
for tx,t in enumerate(transicoesQfinal, start=0):
    for ti in t:
        ti[0]= tx

print("\n Transicoes Finais:")    


estadosFinais= remove_repetidos(estadosFinais)
estadosFinais= ['q'+str(i) for i in estadosFinais]   
estadoInicialNovo= ['q'+str(i) for i in estadoInicialNovo]
for t in  transicoesQfinal:
    for tt in t:        
        tt[0]='q'+str(tt[0])
        tt[1]= novoEstados[tt[1]]
        tt[1]='q'+str(tt[1])        
        tt[2]= alfabeto[tt[2]]        
    if(tt[0] in estadosFinais):
        print (t," Estado Final",end="")
        if(tt[0] in estadoInicialNovo):
            print ("e Estado Inicial")
        else:
            print(" ")
    else:        
        print (t,end=" ")
        if(tt[0] in estadoInicialNovo):
            print ("Estado Inicial")
        else:
            print(" ")
            
            
