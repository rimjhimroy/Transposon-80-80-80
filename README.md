# Transposon-80-80-80
## Requirements
Python3
Ncbi-blast+  
Biopython

## The scripts `full_blast.py` and `query_coverage.py` should be in path.
Put the following line with the absolute path of Transposon-80-80-80 in the .bashrc or .bash_profile  
`export PATH=PATH/TO/Transposon-80-80-80:$PATH`  

## Minimalist installation of dependencies using conda
### Setup Conda (you have to do it only once)
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh 
conda config --set auto_activate_base False
conda update conda

### Get the required conda channels (you have to do it only once)
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

## Create a new conda environment
conda create -n test blast python=3 biopython

## Activate envitonment
conda activate blast
 
## Usage
```
full_blast.py [-h] -query blast_query -subject blast_subject -program  
                     blast_program [-blastout blast_output_path]  
                     [-identity identity_cutoff]  
                     [-querycov query_coverage_cutoff] [-hitlength hit_length]  
                     [-num_threads number_of_threads]  
full_blast.py: error: the following arguments are required: -query, -subject, -program  
```
