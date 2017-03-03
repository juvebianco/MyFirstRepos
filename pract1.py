#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:03:19 2017

@author: manugtorres
"""

import csv
import math
""" Leemos los ficheros """
fichero_peliculas = csv.reader(open('movie-titles.csv', 'rb'))

peliculas = dict()

for index, row in enumerate(fichero_peliculas):
    peliculas[row[0]] = row[1]

fichero_user = csv.reader(open('users.csv', 'rb'))

usuarios = dict()

for index, row in enumerate(fichero_user):
    usuarios[row[0]] = row[1]
    
fichero_tags = csv.reader(open('movie-tags.csv', 'rb'))

etiquetas = []
tags = []

for index, row in enumerate(fichero_tags):
    etiquetas +=[(row[0],row[1])]
    if row[1] not in tags:
        tags += [row[1]]

fichero_ratings = csv.reader(open('ratings.csv', 'rb'))

ratings = dict()

for index, row in enumerate(fichero_ratings):
    ratings[(row[0],row[1])] = row[2]   

TF = dict()
IDF = dict()
perfilProducto = dict()
perfilProductoPrima = dict()
perfilUsuario = dict()
w=dict()


print "Hemos obtenido %s peliculas" %(len(peliculas))  
print "Hemos obtenido %s etiquetas" %(len(tags)) 
print "Hemos obtenido %s opiniones" %(len(etiquetas)) 
print "Hemos obtenido %s opiniones distintas" %(len(tags)) 
print "Hemos obtenido %s ratings" %(len(ratings))

def rellenarTF():
    for j in etiquetas:
        if TF.has_key(j):
            TF[j]= TF.get(j)+1
        else:
            TF[j]=1

    return

"""    for i in peliculas:
        for a in tags:
            if (i,a) not in TF:
                TF[(i,a)]= 0 """
                
def rellenarIDF():
    for i in tags:
        count = 0
        for j in TF:
            if j[1] == i:
                if TF[j] > 0:
                    count = count + 1
        
        IDF[i] = math.log10(len(peliculas)/count)
    
    return

def rellenarPerfilProducto():
    for i in peliculas:
        for j in tags:
            perfilProducto[(i,j)] = TF[(i,j)] * IDF[j]
    return

def normalizarPerfilProducto(): 
    for i in peliculas:
        count = 0
        for j in tags:
            count = count + (perfilProducto[(i,j)] ** 2)
        for k in tags:
            perfilProductoPrima[(i,k)]=perfilProducto[(i,k)] / (count**0.5)
    return
    
def calculoW():
    for i in usuarios:
        media = 0
        count = 0
        for j in ratings:
            if j[0] == i:
                media = media + ratings[j]
                count = count + 1
        media=media/count
        
        for k in peliculas:
            w[(i,k)] = ratings[(i,k)] - media
    return
    
def rellenarPerfilUsuario():
    for i in usuarios:
        for j in tags:
            suma = 0
            for k in peliculas:
                suma = suma + (perfilProductoPrima[(k,j)] * w[(i,k)])
            perfilUsuario[(i,j)] = suma
    return
    
rellenarTF()
rellenarIDF()    
rellenarPerfilProducto()
normalizarPerfilProducto()
calculoW()
rellenarPerfilUsuario()