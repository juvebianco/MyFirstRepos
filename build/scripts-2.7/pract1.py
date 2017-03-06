#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:03:19 2017

@author: manugtorres
"""

import csv
import math

# Leemos los ficheros """
fichero_peliculas = csv.reader(open('movie-titles.csv', 'rb'))

peliculas = []
peliculasID = []

for index, row in enumerate(fichero_peliculas):
    peliculas += [(row[0],row[1])]
    peliculasID += [row[0]]

fichero_user = csv.reader(open('users.csv', 'rb'))

usuarios = []
usersID = []

for index, row in enumerate(fichero_user):
    usuarios += [(row[0],row[1])]
    usersID += [row[0]]
    
fichero_tags = csv.reader(open('movie-tags.csv', 'rb'))

etiquetas = []
tags = []
tags2 = []

for index, row in enumerate(fichero_tags):
    etiquetas +=[(row[0],row[1])]
    tags += [row[1]]

# Quitamos los duplicados
tags2 =list(set(etiquetas))
tags = list(set(tags))


fichero_ratings = csv.reader(open('ratings.csv', 'rb'))

ratings = []
ratingsID = []
ratings_users = dict()
ratings_usersID = []

for index, row in enumerate(fichero_ratings):
    ratings += [((row[0],row[1]),float(row[2]))]  
    ratingsID += [(row[0],row[1])]
    if row[0] in ratings_users:
    #if ratings_users.has_key(row[0]):
        ratings_users[row[0]] = ratings_users.get(row[0]) + float(row[2])
    else:
        ratings_users[row[0]] = float(row[2])
    ratings_usersID +=[row[0]]

TF = []

IDF = [] #dict()

perfilProducto = [] # dict()

perfilProductoPrima = [] #dict()

w = []

perfilUsuario = [] #dict()

perfilUsuarioPrima = [] #dict()

print "Hemos obtenido %s peliculas" %(len(peliculas))  
print "Hemos obtenido %s etiquetas" %(len(etiquetas)) 
print "Hemos obtenido %s etiquetas distintas" %(len(tags)) 
print "Hemos obtenido %s usuarios" %(len(usuarios)) 
print "Hemos obtenido %s ratings" %(len(ratings))


def rellenarTF():
    matrizTF=[]
    for i in tags2:
        matrizTF += [[i, etiquetas.count(i)]]
    return matrizTF

TF = rellenarTF()

print "TF finished"
#print len(tags2)
#print len(TF)
#for i in range(5):
#    print TF[i]," --> ",TF[i][0]," --:> ",TF[i][1]
       

        
def rellenarIDF():
    matrizIDF = []
    for i in tags:
        contar = 0
        for j in TF:
            if j[0][1] == i:
                contar = contar + 1
        
        matrizIDF +=[[i, math.log10(len(peliculas)/contar)]]
    return matrizIDF

IDF = rellenarIDF()

print "IDF finished"

#for i in range(5):
#    print IDF[i]," --> ",IDF[i][0]," --:> ",IDF[i][1]


def rellenarPerfilProducto():
    matrizPerfilProducto = []
 #   for i in peliculas:
    for j in tags2:
        #if (i,j) in tags2:
        matrizPerfilProducto+=[[j, (TF[tags2.index(j)][1] * IDF[tags.index(j[1])][1])]]
        #else:
        #    matrizPerfilProducto+=[[(i,j), 0]]
    return matrizPerfilProducto

perfilProducto = rellenarPerfilProducto()
print "PP finished"
#for i in range(5):
#    print perfilProducto[i]," --> ",perfilProducto[i][0]," --:> ",perfilProducto[i][1]

#if (peliculas[2][0],tags[23]) in tags2:
#    text = perfilProducto[tags2.index((peliculas[2][0],tags[23]))]
#else:
#    text = "("+str(peliculas[2])+","+str(tags[23])+"), 0"
#print peliculas[2]," ---> ",tags[23]," ---:> ",text
   

def normalizarPerfilProducto(): 
    matrizPerfilProductoPrima = []
    for i in peliculas:
        cuenta = 0
        for j in perfilProducto:
            if i[0] == j[0][0]:
                cuenta = cuenta + (j[1] ** 2)
        for k in perfilProducto:
            if i[0] == k[0][0]:
                matrizPerfilProductoPrima += [[k[0],(k[1] / (cuenta**0.5))]]
                
    return matrizPerfilProductoPrima

perfilProductoPrima = normalizarPerfilProducto()
print "PP' finished"
#for i in range(5):
#    print perfilProductoPrima[i]," --> ",perfilProductoPrima[i][0]," --:> ",perfilProductoPrima[i][1]

"""
def calculoW():
    matrizW = []
    for i in ratingsID:
        matrizW+=[[i, (ratings[ratingsID.index(i)][1] - (ratings_users.get(i[0])/ratings_usersID.count(i[0])))]]
    
    for i in usersID: #usuarios:
        media = (ratings_users.get(i)/ratings_usersID.count(i))
        for k in peliculasID:
            if (i,k) in ratingsID:
                matrizW+=[[(i,k), (ratings[ratingsID.index((i,k))][1] - media)]]
            else: 
                matrizW+=[[(i,k), -media]]
    
    return
w=calculoW()    
for i in range(5):
    print w[i]," --> ",w[i][0]," --:> ",w[i][1]
"""
def rellenarPerfilUsuario(i):
    matrizPU = []
    for j in tags2:
        suma = 0
        w = 0
        media = (ratings_users.get(i)/ratings_usersID.count(i))
        if (i,j[1]) in ratings_users:
            w = ratings[ratingsID.index((i,j[0]))][1] - media
        else:
            w = -media
        suma = suma + (perfilProductoPrima[[y[0] for y in perfilProductoPrima].index((j))][1] * w)
        matrizPU += [[j, suma]]
    print "PU finished"
    return matrizPU
#2perfilUsuario = rellenarPerfilUsuario('500')
#print "PU finished"

def normalizarPerfilUsuario(pu): 
    matrizPerfilUsuarioPrima = []
    cuenta = 0
    for j in pu:
        cuenta = cuenta + (j[1] ** 2)
    for k in pu:
        matrizPerfilUsuarioPrima += [[k[0],(k[1] / (cuenta**0.5))]]
                
    print "PU' finished"
    return matrizPerfilUsuarioPrima

#perfilUsuarioPrima = normalizarPerfilUsuario()
#print "PU' finished"

def vectorNoValorado(user):
    vector = []
    for i in peliculasID:
        if (user,i) not in ratingsID:
            vector += [i]
    return vector
    
def recomendacion(user):
    cos = []
    pu = rellenarPerfilUsuario(user)
    pup = normalizarPerfilUsuario(pu)
    vec = vectorNoValorado(user)
    for i in vec:
        suma = 0
       # suma2 = 0
       # suma3 = 0
        for j in tags2:
            suma = suma + (pup[[y[0] for y in pup].index((j))][1] * perfilProductoPrima[[y[0] for y in perfilProductoPrima].index((j))][1])
        #    suma2 = suma2 + (perfilUsuarioPrima[(user,i)]**2)
        #    suma3 = suma3 + (perfilProductoPrima[(i,j)]**2)
        cos += [[i, suma]] # /((suma2**0.5)*(suma3**0.5)))
        
    cos.sort()
    print "Las recomendaciones para el usuario ", user, "son:"
    for a in range(10):
        print peliculas[peliculasID.index(cos[a][0])][1],": ",cos[a][1]
    
    return
  


stop = 1
while stop > 0:
    user = input("Introduzca perfil de usuario (0 para salir): ")
    if user > 0:
        recomendacion(str(user))
    stop = user