import sys
import numpy as np
import pandas as pd
from manipularArquivo import *
from removerRepetidos import *



arquivo=manipularArquivo()
alfabeto = arquivo[0]
estados = arquivo[1]
inicial = arquivo[2]
final = arquivo[3]
transicoes = arquivo[4]


## Vefificações do arquivo
if not ((len(estados)*2) == len(transicoes)):
    sys.exit("Numero incorreto de transicoes")
if (len(inicial) > 1):
    sys.exit("Mais de um estado inicial")
if (len(final) > len(estados)):
    sys.exit("Numero de estados finais incorreto")

count= np.full((len(estados)), 0)
for t in transicoes:
    count[t[0]]= count[t[0]] + 1
for c in count:
    if(c > 2):
        sys.exit("Numero de transições saindo de um mesmo estado maior que o permitido")
    if(c < 2):
        sys.exit("Numero de transições saindo de um mesmo estado menor que o permitido")

## Criando Matriz para manipulação
matrizTamanho = len(estados)
matriz = np.full((matrizTamanho,matrizTamanho), 0)
print("\n Matriz vazia com a quantidade de espaços variando de acordo com os numero de estados. \n",matriz,"\n")   


## Setando 1 para todos os pares (L,C) onde L é final e C não é final.
## Setando 0 se L e C são Finais.     
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
print("\n Setando 1 para todos os pares (L,C) onde L é final e C não é final. \n",matriz,"\n")     


## Verifica onde ainda é 0 na matriz e ver se (L,C) onde [(L,x),(C,x)] é 1 se for então (L,C) tambés vira 1. 
                                                    
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
                
print("Verifica onde ainda é 0 na matriz e ver se (L,C) onde [(L,x),(C,x)] é 1 se for então (L,C) tambés vira 1. \n",matriz,"\n")                    

## Criando matriz ignorando a diagonal superior
matrizDiag = np.tri(matrizTamanho,matrizTamanho)
for idx,x in enumerate(matrizDiag, start=0):
        for idy,y in enumerate(matrizDiag, start=0):  
            if(matrizDiag[idx][idy] == 0): 
                matriz[idx][idy] = 999 
            if(idx == idy): 
                matriz[idx][idy] = 999     
                
print("Nova matriz ignorando a diagonal superior. \n",matriz,"\n")       


## Lista onde é 0 na Matriz
listJuntar = []
for idx,x in enumerate(matriz, start=0):
        for idy,y in enumerate(matriz, start=0):  
            if(matriz[idx][idy] == 0):
                listJuntar.append([idy,idx]) 

print ("Criando uma nova lista onde é 0 na Matriz",listJuntar,"\n")             




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
                                             
print ("Novo Conjunto de estados finais \n",estadosQfinal,"\n")    

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

matrizFinal = np.full((nEstado,nEstado), "")     

for t in  transicoesQfinal:
    for tt in t:                
        tt[0]='q'+str(tt[0])
        tt[1]= novoEstados[tt[1]]
        tt[1]='q'+str(tt[1])        
        tt[2]= alfabeto[tt[2]]        
    if(tt[0] in estadosFinais):          
         
        
        x1=int((t[0][0])[1:])
        x2=int((t[0][1])[1:])
        y1=int((t[1][0])[1:])
        y2=int((t[1][1])[1:])        
        matrizFinal[x1][x2]=matrizFinal[x1][x2]+ t[0][2] 
        matrizFinal[y1][y2]=matrizFinal[y1][y2]+ t[1][2]            
                       
        print (t," Estado Final",end="")
        if(tt[0] in estadoInicialNovo):
            
            print ("e Estado Inicial")
        else:
            print(" ")
    else:        
        x1=int((t[0][0])[1:])
        x2=int((t[0][1])[1:])
        y1=int((t[1][0])[1:])
        y2=int((t[1][1])[1:])        
        matrizFinal[x1][x2]=matrizFinal[x1][x2]+ t[0][2] 
        matrizFinal[y1][y2]=matrizFinal[y1][y2]+ t[1][2]        
             
        print (t,end=" ")
        if(tt[0] in estadoInicialNovo):
            print ("Estado Inicial")
        else:
            print(" ")        


DF = pd.DataFrame(matrizFinal)
DF.to_csv("tabelaParaVizualizacao.csv")
