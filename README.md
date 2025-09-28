# Análisis de Base de Datos de Hongos (ITS)

Este repositorio contiene scripts en Python para el análisis y procesamiento de una base de datos curada de secuencias de hongos en formato FASTA comprimido (`.fasta.gz`). Los scripts permiten explorar, resumir y transformar la base de datos para su posterior análisis.

## CONTENIDO 



### 1. Resumen de las primeras secuencias
**Archivo sugerido:** `scripts/resumen_fasta.py`

**Descripción:**  
Este script permite visualizar los primeros encabezados y las secuencias iniciales de la base de datos `.fasta.gz` para tener un vistazo rápido de cómo se ve el archivo. Solo muestra una cantidad limitada de secuencias para no saturar la salida.

##2. Conteo de secuencias por Phylum

Archivo sugerido: scripts/conteo_phyla.py

Descripción:
Cuenta cuántas secuencias corresponden a cada phylum de hongos en la base de datos. Esto permite identificar la distribución taxonómica general y cuántas secuencias no están clasificadas.

### 3. Conversión de FASTA a TSV ordenado por Phylum

Archivo sugerido: scripts/fasta_a_tsv.py

Descripción:
Convierte la base de datos .fasta.gz a un archivo tabulado (.tsv) con las columnas ID, Phylum y Secuencia. Además, ordena el archivo resultante alfabéticamente por phylum para facilitar análisis posteriores.
