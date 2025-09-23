def fasta_to_tsv_gz(fasta_file, output_file="hongos.tsv"):
    data = []

    with gzip.open(fasta_file, "rt") as f:
        seq_id, seq, phylum = None, [], None
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                # Guardar la secuencia anterior si existe
                if seq_id and phylum:
                    data.append([seq_id, phylum, "".join(seq)])

                # Reiniciar
                seq = []
                header = line[1:]
                parts = header.split(";")

                seq_id = parts[0].split()[0]  # ID
                phylum = parts[2] if len(parts) > 2 else "Unclassified"
            else:
                seq.append(line)

        # Guardar la última
        if seq_id and phylum:
            data.append([seq_id, phylum, "".join(seq)])

    # Convertir a DataFrame
    df = pd.DataFrame(data, columns=["ID", "Phylum", "Secuencia"])

    # Ordenar por Phylum
    df = df.sort_values(by="Phylum")

    # Guardar como TSV
    df.to_csv(output_file, sep="\t", index=False)

    print(f"✅ Archivo TSV generado: {output_file}")
    return df

# Ejemplo de uso:
fasta_to_tsv_gz("ITS.fasta.gz", "hongos.tsv")

