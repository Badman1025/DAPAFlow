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
- **`-i`** [Testdata](https://github.com/Badman1025/APAFlow/tree/main/test).  
- **`-t`** TarBase_3UTR.tsv(output of APAFlow) 

```
python deAPAFlow.py -i aUTRWithdPAS_pPAS.csv -g Homo_sapiens.GRCh38.dna.primary_assembly.fa -t TarBase_3UTR.tsv -m ./miRNA_meme/Homo_sapiens_hsa.meme -n 3 -o test
```
## Result
![image](https://github.com/user-attachments/assets/0606af2f-4166-4bdc-97c2-eeba68224769)

## Citation
1. article
2. Timothy L. Bailey and Charles Elkan, "Fitting a mixture model by expectation maximization to discover motifs in biopolymers", Proceedings of the Second International Conference on Intelligent Systems for Molecular Biology, pp. 28-36, AAAI Press, Menlo Park, California, 1994.
