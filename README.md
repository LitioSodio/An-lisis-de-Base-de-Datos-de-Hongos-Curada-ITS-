# Análisis de Base de Datos de Hongos (ITS)

Este repositorio contiene scripts en Python para el análisis y procesamiento de una base de datos curada de secuencias de hongos en formato FASTA comprimido (`.fasta.gz`). Los scripts permiten explorar, resumir y transformar la base de datos para su posterior análisis.
La entrada principal es un archivo FASTA comprimido (ITS.fasta.gz).
La salida principal es un archivo tabulado (.tvs o .tsv) con información organizada de cada secuencia (ID, taxonomía y secuencia).


Análisis-de-Base-de-Datos-de-Hongos-Curada-ITS-/
│
├── scripts/                  # Scripts principales en Python
│   ├── resumen_fasta.py      # Genera un resumen básico de las secuencias en el FASTA
│   ├── conteo_phyla.py       # Cuenta y clasifica secuencias según el phylum
│   └── fasta_a_tvs.py        # Convierte el FASTA en un archivo tabulado (TSV/TVS)
│
├── ITS.fasta.gz              # Archivo FASTA curado con secuencias ITS de hongos
├── Hongosresumen.tvs         # Ejemplo de salida tabulada
├── README.md                 # Este archivo
└── .gitignore

Contenidos del tvs generado con el script fasta_a_tvs.py 

ID -> Nombre del género y la especie del hongo y el ID del mismo 
Phylum -> Reino y clase a la que pertenece el hongo 
Secuencia -> Codigo génetico del hongo


##Requisitos / Dependencias

Python 3.8 o superior

Librerías necesarias:

pandas

se recomienda instalar dependencias con: 
pip install -r 

## Uso/Ejecucion 

# 1. Ver un resumen rápido de la base de datos
python scripts/resumen_fasta.py ITS.fasta.gz

# 2. Contar secuencias por phylum
python scripts/conteo_phyla.py ITS.fasta.gz

# 3. Convertir el FASTA curado a tabla (TSV/TVS)
python scripts/fasta_a_tvs.py ITS.fasta.gz Hongosresumen.tvs

# 4. Revisar las primeras líneas del archivo generado
head -n 10 Hongosresumen.tvs

