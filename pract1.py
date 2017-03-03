#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:03:19 2017

@author: manugtorres
"""

import csv

fichero_peliculas = csv.reader(open('rs-cour-dataset/movie-titles.csv', 'rb'))

peliculas = dict()

for index, row in enumerate(fichero_peliculas):
    peliculas[row[0]] = row[1]

fichero_user = csv.reader(open('rs-cour-dataset/users.csv', 'rb'))

usuarios = dict()

for index, row in enumerate(fichero_user):
    usuarios[row[0]] = row[1]
    
fichero_tags = csv.reader(open('rs-cour-dataset/movie-tags.csv', 'rb'))

etiquetas = []
tags = dict()

for index, row in enumerate(fichero_tags):
    etiquetas +=[(row[0],row[1])]
    tags[row[1]] = ""

fichero_ratings = csv.reader(open('rs-cour-dataset/ratings.csv', 'rb'))

ratings = dict()

for index, row in enumerate(fichero_ratings):
    ratings[(row[0],row[1])] = row[2]   
"""
TF = dict()
"""

print "Hemos obtenido %s peliculas" %(len(peliculas))  
print "Hemos obtenido %s etiquetas" %(len(tags)) 
print "Hemos obtenido %s opiniones" %(len(etiquetas)) 
print "Hemos obtenido %s opiniones distintas" %(len(tags)) 
print "Hemos obtenido %s ratings" %(len(ratings))
"""
def rellenarTF():
    for j in etiquetas:
        if TF.has_key(j):
            TF[j]= TF.get(j)+1
        else:
            TF[j]=1

    for i in peliculas:
        for a in tags:
            if (i[0],a) not in TF:
                TF[(i[0],a)]=0
    return
rellenarTF()    
print tags
print TF

print len(peliculas)
print len(usuarios)
print len(etiquetas)
print len(tags)
"""