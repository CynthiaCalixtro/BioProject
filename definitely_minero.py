#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:27:58 2018

@author: HAZARD , CYNTHIA AND ALEXANDRA !!!
"""

import os
import sys
from os import walk
from Bio import Entrez

def depura_pais_conjunto_especies_existentes (name_archivo):
 archivo = open(name_archivo, "r")
 animales = []
 for linea in archivo.readlines():
  animal = linea
  search_string = animal+"[Organism]"
  #search_string = item+"[Gene] AND "+animal+"[Organism] AND mRNA[Filter] AND RefSeq[Filter]"
  handle= Entrez.esearch(db="nucleotide", term=search_string)
  record = Entrez.read(handle)
  ids = record['IdList']
  if  len (ids) > 0 :
   animales.append(animal)
 archivo.close()
 salida= open(name_archivo.replace("FAUNA_ENDEMICA_","fauna_endemica_"),"a") 		
 for linea in animales:
  animal = linea
  search_string = animal+"[Organism]"
  handle1= Entrez.esearch(db="protein", term=search_string)
  record = Entrez.read(handle1)
  ids = record['IdList']
  if  len(ids) >0 :
   salida.write(animal[:len(animal)-1])
   salida.write('\n')
 salida.close()		

def minero_extrae_fasta_proteina_gen_conjunto_especies (name_archivo , ruta_destino):
 archivo = open(name_archivo, "r")
 # --------------- GENERANDO ARCHIVOS FASTA DE GENES Y PROTEINAS
 
 for item in archivo.readlines():
  animal = item
  os.mkdir(ruta_destino + "/" + animal[:len(item)-1])
  search_string = animal+"[Organism]"
  handle= Entrez.esearch(db="nucleotide", term=search_string)
  record = Entrez.read(handle)
  ids = record['IdList']
  genes=open(ruta_destino + "/" + animal[:len(item)-1] + "/"+ animal[:len(item)-1] + "_GENES",'a')
  for gen in ids:
   handle = Entrez.efetch(db="nucleotide", id=gen, rettype="fasta", retmode="text")
   record = handle.read()
   name_arch = ruta_destino + "/" + animal[:len(item)-1] + "/"+  "GEN_"+item[:len(item)-1] + "_" + gen + ".fasta"
   out_handle = open(name_arch, 'w')
   out_handle.write(record.rstrip('\n'))
   out_handle.close()
   genes.write(gen)
   genes.write('\n')
   
  genes.close()
  #search_string = item+"[Gene] AND "+animal+"[Organism] AND mRNA[Filter] AND RefSeq[Filter]"
  handle1= Entrez.esearch(db="protein", term=search_string)
  record1 = Entrez.read(handle1)
  ids1 = record1['IdList']
  proteinas=open(ruta_destino + "/" + animal[:len(item)-1] + "/"+ animal[:len(item)-1] + "_PROTEINAS", 'a')
  for proteina in ids1:
   handle1 = Entrez.efetch(db="protein", id=proteina, rettype="fasta", retmode="text")
   record1 = handle1.read()
   name_arch2 = ruta_destino + "/" + animal[:len(item)-1] + "/"+ "PROTEIN_" + item[:len(item)-1] + "_"  + proteina + ".fasta"
   out_handle = open(name_arch2, 'w')
   out_handle.write(record1.rstrip('\n'))
   out_handle.close()
   proteinas.write(proteina)
   proteinas.write('\n')
  proteinas.close()
 archivo.close()


def DEPURADOR_PAISES():

 buscar = "FAUNA_ENDEMICA_"
 directorio = os.getcwd()
 if(len(sys.argv) > 1):
  if(not os.path.isdir(sys.argv[1])):
  	print(sys.argv[1],"no se reconoce como directorio")
  	sys.exit(1)
  directorio = sys.argv[1]
 for arch in next(walk(directorio))[2]:
 	if(buscar in arch):
 		depura_pais_conjunto_especies_existentes(arch)

def ACTUALIZADOR_UNIVERSAL_creador_arbol_carpetas_archivos():

 buscar = "fauna_endemica_"
 directorio = os.getcwd()
 if(len(sys.argv) > 1):
  if(not os.path.isdir(sys.argv[1])):
  	print(sys.argv[1],"no se reconoce como directorio")
  	sys.exit(1)
  directorio = sys.argv[1]
 for arch in next(walk(directorio))[2]:
 	if(buscar in arch):
		nombre_archivo_fauna=arch
		nombre_carpeta_pais=arch.replace("fauna_endemico_", "")
		os.mkdir(nombre_carpeta_pais)
 		minero_extrae_fasta_proteina_gen_conjunto_especies(nombre_archivo_fauna,nombre_carpeta_pais)


DEPURADOR_PAISES()
ACTUALIZADOR_UNIVERSAL_creador_arbol_carpetas_archivos()

