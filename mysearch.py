#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:51:00 2018

@author: chia
"""

# Sistema de consultas  
from Bio import Entrez
Entrez.email = "cylthchi@gmail.com"

################################
# buscando nucleotidos
# Creando una lista para guardar ...
mylist = ""

# Lee el documento de texto y guardarlo en pais
pais = open('/home/alexandra/Escritorio/jamaica.txt','r')

# Linea es una cadena de caracteres que recorrera linea por linea a pais 
for linea in pais.readlines():
    n = len(linea)  # n es la longitud de la cadea de una linea 
    especie = linea[0:n-1]    # especie guarda el nombre de la especie de una linea 
    search_string = especie+"[Organism]"  
    
    handleN = Entrez.esearch(db="nucleotide", term=search_string) # con esearch buscamos en entrez en la base nucleotido y recupera los items de cada especie y lo guarda en handleN
    recordN = Entrez.read(handleN)  # read analiza el archivo handleN y lo guarda en recordN 
    idsN = recordN['IdList']     # idsN guardara los Ids que contiene una especie 
    
    handleP = Entrez.esearch(db="protein", term=search_string) # analogo para la base de datos proteina 
    recordP = Entrez.read(handleP)
    idsP = recordP['IdList']
    
    # Si en ambos no esta vacia las listas se guarda 
    if (idsN != []) &(idsP != []):
        print(especie)
        mylist = mylist + especie + "\n"  # guardamos todas las especies que tienen nucleotidos y proteinas  en mylist
pais.close()  

nucleotidos = open('/home/chia/BioloCompu/Proyecto/nucleotidos.txt','w')
nucleotidos.write(mylist)
nucleotidos.close()
