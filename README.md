# Transposon-80-80-80
## Requirements
Python3  
Ncbi-blast+    
Biopython  

### Installation.
sudo python3 -m pip install dist/transposon80_80_80-0.1-py3-none-any.whl  

## Minimalist installation of dependencies using conda
### Setup Conda (you have to do it only once)
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh 
conda config --set auto_activate_base False
conda update conda
```
### Get the required conda channels (you have to do it only once)
```
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
```

### Create a new conda environment (you have to do it only once)
```
conda create -n blast blast python=3 biopython
```

## Activate envitonment
```
conda activate blast
```
 
## Usage
```
 full_blast [-h] -q blast_query -s blast_subject -p blast_program
                     [-o blast_output_path] [-i identity_cutoff]
                     [-qc query_coverage_cutoff] [-l hit_length]
                     [-t number_of_threads]

This script takes a query and a database file for blastn/megablast and parses it

optional arguments:
  -h, --help            show this help message and exit
  -q blast_query, --query blast_query
                        REQUIRED: Full path to query file
  -s blast_subject, --subject blast_subject
                        REQUIRED: Full path to subject file
  -p blast_program, --program blast_program
                        REQUIRED: blast program to use blastn/megablast
  -o blast_output_path, --blastout blast_output_path
                        full path to blast output folder to store in -outfmt 6/ -m8 format [DEFAULT: ./outblast]
  -i identity_cutoff, --identity identity_cutoff
                        Minimum identity cutoff in % [DEFAULT: 80]
  -qc query_coverage_cutoff, --querycov query_coverage_cutoff
                        Minimum query coverage cutoff in % [DEFAULT: 20]
  -l hit_length, --hitlength hit_length
                        Minimum hit length cutoff in bps [DEFAULT: 80]
  -t number_of_threads, --num_threads number_of_threads
                        Maximum number of threads [DEFAULT: 4]
                        
the following arguments are required: -q/--query, -s/--subject, -p/--program
```
