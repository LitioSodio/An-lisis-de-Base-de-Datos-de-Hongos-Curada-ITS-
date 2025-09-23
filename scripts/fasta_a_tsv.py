import gzip
from collections import Counter


def contar_phyla(fasta_file, compressed=True):
    # Soporte para .fasta y .fasta.gz
    open_func = gzip.open if compressed else open

    phylum_counts = Counter()

    with open_func(fasta_file, "rt") as f:
        for line in f:
            if line.startswith(">"):
                # Quitamos el ">" y partimos el encabezado
                parts = line[1:].strip().split(";")
                if len(parts) > 2:
                    phylum = parts[2]  # Normalmente el phylum está en la 3ra posición
                    phylum_counts[phylum] += 1
                else:
                    phylum_counts["Unclassified"] += 1

    # Mostrar resultados
    print("Secuencias por Phylum:")
    for phylum, count in phylum_counts.most_common():
        print(f"{phylum}: {count}")

    return phylum_counts


# Ejemplo de uso
# Si tu archivo es .fasta.gz
contar_phyla("ITS.fasta.gz", compressed=True)
