#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:03:19 2017

@author: manugtorres
"""
peliculas = [(1,"batman"),(2,"pretty woman"),(3,"beatlejuece")]
usuarios = []
etiquetas = [(1,"romantica"),(2,"comedia"),(1,"terror"),(1,"romantica")]
rating = []

tags = []

TF = dict()

for a in etiquetas:
    text = a[1]

    if text not in tags:
        tags += [a[1]]

print "Hemos obtenido %s peliculas" %(len(peliculas))  
print "Hemos obtenido %s etiquetas" %(len(tags)) 
print "Hemos obtenido %s opiniones" %(len(etiquetas)) 
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
