#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:03:19 2017

@author: manugtorres
"""
peliculas = [1,2,3]
usuarios = []
etiquetas = [(1,"romantica"),(2,"comedia"),(1,"terror"),(1,"romantica")]
rating = []

tags = dict()

TF = dict()

tags = {
    (1,"a"):3,
    (1,"b"):5,
    (2,"a"):1,
    (3,"a"):6    
}

for a,b in tags.items():
    for c in a[1]:
        print "(%s, %s) - > %s" %(a[0],c,b)
        
if tags.has_key((1,"a")):
    tags[(1,"a")]= tags.get((1,"a"))+1
    print "si"
    print tags.get((1,"a"))
else:
    print "no"
    
def rellenarTF():
    for i in peliculas:
        for j in etiquetas:
            if i == j[0]:
                if TF.has_key((i,j[1])):
                    TF[(i,j[1])]= TF.get((i,j[1]))+1
                else:
                    TF[(i,j[1])]=1
            else:
                TF[(i,j[1])]=0
    return
rellenarTF()    
print TF
