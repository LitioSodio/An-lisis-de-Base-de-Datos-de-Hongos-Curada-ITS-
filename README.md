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
import gzip
from itertools import islice

# Nombre de tu archivo fasta.gz
fasta_file = "data/ITS.fasta.gz"

# Mostrar las primeras 5 secuencias
mostrar_fasta(fasta_file, n=5)


