import csv
import argparse
import subprocess
import os

def csv_to_bed(input_csv_file, output_bed_file):
    with open(input_csv_file, mode='r', newline='', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader, None)
        with open(output_bed_file, mode='w', newline='', encoding='utf-8') as outfile:
            for row in csv_reader:
                chromosome = row[0]
                start = row[1]
                end = row[2]
                gene_name = row[3] if len(row) > 3 else '.'
                outfile.write(f"{chromosome}\t{start}\t{end}\t{gene_name}\n")

def run_bedtools_getfasta(genome_fasta, bed_file, output_fasta):
    command = [
        "bedtools", "getfasta",
        "-fi", genome_fasta,
        "-bed", bed_file,
        "-fo", output_fasta
    ]
    subprocess.run(command, check=True)

def run_meme(input_fasta, output_dir, nmotifs):
    command = [
        "meme", input_fasta,
        "-o", output_dir,
        "-rna",
        "-nmotifs", str(nmotifs)
    ]
    subprocess.run(command, check=True)

def run_tomtom(meme_file, motif_db, output_tomtom):
    command = [
        "tomtom", meme_file, motif_db,
        "-o", output_tomtom
    ]
    subprocess.run(command, check=True)

def filter_tarbase(gene_file, tarbase_file, output_file):
    with open(gene_file, mode='r', encoding='utf-8') as infile:
        gene_names = set(line.strip() for line in infile)
    with open(tarbase_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        header = lines[0]
        outfile.write(header)
        for line in lines[1:]:
            columns = line.strip().split('\t')
            if len(columns) >= 4 and columns[3] in gene_names:
                outfile.write(line)

def filter_tomtom(tomtom_file, deTarBase_file, output_file):
    with open(tomtom_file, mode='r', encoding='utf-8') as infile:
        tomtom_ids = set()
        for line in infile:
            columns = line.strip().split('\t')
            if len(columns) >= 2:
                tomtom_ids.add(columns[1])
    with open(deTarBase_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        header = lines[0]
        outfile.write(header)
        for line in lines[1:]:
            columns = line.strip().split('\t')
            if len(columns) >= 2 and columns[1] in tomtom_ids:
                outfile.write(line)

def extract_gene_names(input_csv_file, gene_file):
    with open(input_csv_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(gene_file, mode='w', newline='', encoding='utf-8') as outfile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader, None)  # Skip header
        gene_names = set()
        for row in csv_reader:
            if len(row) >= 4:
                gene_names.add(row[3])
        outfile.write("\n".join(gene_names))

def main():
    parser = argparse.ArgumentParser(description="DAPAFlow: A pipeline for analyzing differential 3'UTR APA related data (eg.cUTR/aUTR).")
    parser.add_argument("-i", "--input_csv", required=True, help="Input CSV file containing APA information.")
    parser.add_argument("-g", "--genome_fasta", required=True, help="Genome FASTA file.")
    parser.add_argument("-t", "--tarbase_file", required=True, help="TarBase file.")
    parser.add_argument("-m", "--meme_motif_db", required=True, help="MEME motif database file.")
    parser.add_argument("-o", "--output_dir", default="output", help="Output directory for results. Default: output")
    parser.add_argument("-n", "--nmotifs", type=int, default=10, help="Number of motifs to search for in MEME. Default: 10")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # Extract gene names from the input CSV file
    gene_file = os.path.join(args.output_dir, "gene.txt")
    extract_gene_names(args.input_csv, gene_file)

    bed_file = os.path.join(args.output_dir, "de3UTR.bed")
    csv_to_bed(args.input_csv, bed_file)

    fasta_file = os.path.join(args.output_dir, "de3UTRAPA.fa")
    run_bedtools_getfasta(args.genome_fasta, bed_file, fasta_file)

    meme_output_dir = os.path.join(args.output_dir, "MEME")
    run_meme(fasta_file, meme_output_dir, args.nmotifs)

    meme_file = os.path.join(meme_output_dir, "meme.txt")
    tomtom_output = os.path.join(args.output_dir, "tomtom")
    run_tomtom(meme_file, args.meme_motif_db, tomtom_output)

    deTarBase_file = os.path.join(args.output_dir, "deTarBase_3UTR.tsv")
    filter_tarbase(gene_file, args.tarbase_file, deTarBase_file)

    tomtom_file = os.path.join(tomtom_output, "tomtom.tsv")
    final_tarbase_file = os.path.join(args.output_dir, "Final_TarBase_3UTR.tsv")
    filter_tomtom(tomtom_file, deTarBase_file, final_tarbase_file)

if __name__ == "__main__":
    main()
