# Análisis de Base de Datos de Hongos (ITS)

Este repositorio contiene scripts en Python para el análisis y procesamiento de una base de datos curada de secuencias de hongos en formato FASTA comprimido (`.fasta.gz`). Los scripts permiten explorar, resumir y transformar la base de datos para su posterior análisis.

---

## Estructura del repositorio sugerida

- `data/` : Archivos de entrada, por ejemplo `ITS.fasta.gz`.
- `scripts/` : Scripts en Python para análisis de datos.
- `results/` : Resultados generados por los scripts, como TSV u otros resúmenes.
- `README.md` : Documentación y explicación del repositorio.

---

## Scripts disponibles

### 1. Resumen de las primeras secuencias
**Archivo sugerido:** `scripts/resumen_fasta.py`

**Descripción:**  
Este script permite visualizar los primeros encabezados y las secuencias iniciales de la base de datos `.fasta.gz` para tener un vistazo rápido de cómo se ve el archivo. Solo muestra una cantidad limitada de secuencias para no saturar la salida.

**Uso:**
```python

2. Conteo de secuencias por Phylum

Archivo sugerido: scripts/conteo_phyla.py

Descripción:
Cuenta cuántas secuencias corresponden a cada phylum de hongos en la base de datos. Esto permite identificar la distribución taxonómica general y cuántas secuencias no están clasificadas.

Uso:

from collections import Counter
import gzip

# Contar secuencias por phylum
conteo = contar_phyla("data/ITS.fasta.gz", compressed=True)


Salida esperada:
Lista de phyla y el número de secuencias correspondientes a cada uno.

3. Conversión de FASTA a TSV ordenado por Phylum

Archivo sugerido: scripts/fasta_a_tsv.py

Descripción:
Convierte la base de datos .fasta.gz a un archivo tabulado (.tsv) con las columnas ID, Phylum y Secuencia. Además, ordena el archivo resultante alfabéticamente por phylum para facilitar análisis posteriores.

Uso:

import pandas as pd
import gzip

# Convertir y guardar como TSV
df = fasta_to_tsv_gz("data/ITS.fasta.gz", "results/hongos.tsv")


