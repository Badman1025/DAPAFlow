# DAPAFlow
DAPAFlow (Differential APA Flow) is a pipeline designed for analyzing conserved sequences in differential 3' UTR APA events (cUTR/aUTR) and constructing regulatory networks between miRNAs and their targets.

![image](https://github.com/user-attachments/assets/7f35c6d1-22a9-4e49-8f21-7d198f26e526)

```
python DAPAFlow.py -h
usage: DAPAFlow.py [-h] -i INPUT_CSV -g GENOME_FASTA -t TARBASE_FILE -m MEME_MOTIF_DB [-o OUTPUT_DIR] [-n NMOTIFS]

DAPAFlow: A pipeline for analyzing differential 3'UTR APA related data (eg.cUTR/aUTR).

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
- **`-i`** [aUTR](https://github.com/Badman1025/DAPAFlow/blob/main/aUTRWithdPAS_pPAS.csv).  
- **`-t`** TarBase_3UTR.tsv(output of APAFlow) 

```
python DAPAFlow.py -i aUTRWithdPAS_pPAS.csv -g Homo_sapiens.GRCh38.dna.primary_assembly.fa -t TarBase_3UTR.tsv -m ./miRNA_meme/Homo_sapiens_hsa.meme -n 3 -o test
```
## Result
![image](https://github.com/user-attachments/assets/0606af2f-4166-4bdc-97c2-eeba68224769)

## Expansion
The alternative splicing event location information can be used as input. The "TarBase_3UTR.tsv" file needs to be replaced with "TarBase_CDS.tsv", which is extracted using the "[exact_CDS.py](https://github.com/Badman1025/DAPAFlow/blob/main/exact_CDS.py)" script.
## Citation
1. article
2. Timothy L. Bailey and Charles Elkan, "Fitting a mixture model by expectation maximization to discover motifs in biopolymers", Proceedings of the Second International Conference on Intelligent Systems for Molecular Biology, pp. 28-36, AAAI Press, Menlo Park, California, 1994.
