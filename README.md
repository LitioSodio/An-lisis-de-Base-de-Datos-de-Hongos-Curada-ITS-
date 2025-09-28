# Análisis de Base de Datos de Hongos (ITS)

Este repositorio contiene scripts en Python para el análisis y procesamiento de una base de datos curada de secuencias de hongos en formato FASTA comprimido (`.fasta.gz`). Los scripts permiten explorar, resumir y transformar la base de datos para su posterior análisis.

## CONTENIDO 
README ---> Este archivo con resumen de como usar este repositorio

ITS.fasta.gz --> Base de datos curada de hongos descargada de UNIT

Carpeta Scripts

resumen_fasta --->  script que permite visualizar los primeros encabezados y las secuencias iniciales de la base de datos ITS.fasta.gz para tener un vistazo rápido de cómo se ve el archivo

conteo_phyla.py--->  script que cuenta cuántas secuencias corresponden a cada phylum de hongos en la base de datos

fasta_a_tvs --->  script principal que procesa los datos del archivo fasta.gz a formato .tvs

Hongos.tvs --> tabla resultante luego de correr el script principal fasta_a_tvs.py

