# deAPAFlow
deAPAFlow is a pipeline designed for analyzing conserved sequences in differential 3' UTR APA events (cUTR/aUTR) and constructing regulatory networks involving miRNAs and their targets.

```
python deAPAFlow.py -h
usage: deAPAFlow.py [-h] -i INPUT_CSV -g GENOME_FASTA -t TARBASE_FILE -m MEME_MOTIF_DB [-o OUTPUT_DIR] [-n NMOTIFS]

deAPAFlow: A pipeline for analyzing differential 3'UTR APA related data (eg.cUTR/aUTR).

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_CSV, --input_csv INPUT_CSV
                        Input CSV file containing APA information.
  -g GENOME_FASTA, --genome_fasta GENOME_FASTA
                        Genome FASTA file.
  -t TARBASE_FILE, --tarbase_file TARBASE_FILE
                        TarBase file.
  -m MEME_MOTIF_DB, --meme_motif_db MEME_MOTIF_DB
                        MEME motif database file.
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Output directory for results. Default: output
  -n NMOTIFS, --nmotifs NMOTIFS
                        Number of motifs to search for in MEME. Default: 10
```
# test
