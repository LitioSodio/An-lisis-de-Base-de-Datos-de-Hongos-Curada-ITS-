import gzip
from itertools import islice

# Nombre de tu archivo fasta.gz
fasta_file = "ITS.fasta.gz"

# Función para leer el fasta y mostrar algunos ejemplos
def mostrar_fasta(fasta_file, n=5):
    with gzip.open(fasta_file, "rt") as handle:  # "rt" = leer como texto
        count = 0
        for line in handle:
            if line.startswith(">"):  # Encabezado de la secuencia
                print(f"\nEncabezado: {line.strip()}")
                count += 1
            else:  # Secuencia asociada
                print(f"Secuencia (inicio): {line.strip()[:80]}...")  # solo 80 bases para no saturar
            if count >= n:  # mostramos solo las primeras n secuencias
                break

# Mostrar las primeras # secuencias
mostrar_fasta(fasta_file, n=#)
