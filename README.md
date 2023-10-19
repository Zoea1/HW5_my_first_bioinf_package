# HW6_my_first_bioinf_package
These are my_first_bioinf_package.py tool and bio_files_processor.py. My_first_bioinf_package.py is able to work with protein sequences and DNA sequences, and also is capable of working with fastq files. It imports functions from inner_code folder. bio_files_processor.py can process fasta files.
# Installation
Download my_first_bioinf_package.py, bio_files_processor.py and inner_code folder. You can use this code in your programms. This script cannot work independently, because there is no input from keyboard. 
# Usage
First, a user should choose what kind of operation he or she wants to do. There are three main options in the package:
- to filter fastq sequences (use `filter_fastq` function)
- to convert fasta file with multiline sequence into fasta file with one line sequence (use `convert_multiline_fasta_to_oneline` in `bio_files_processor.py`)
- to change position of a nucleotide in a sequence in fasta file (use `change_fasta_start_pos` in `bio_files_processor.py`)
- to work with protein sequence(s) (use `protein_tools` function)
- to work with protein sequence(s) (use `run_rna_dna_tools`)
Next, there are several options inside some of the chosen functions.

For `run_rna_dna_tools`:
The function`s input consists of an unlimited number of arguments, where all of them are DNA sequences except the last, which is the name of the action a user wants to do on the sequences. The list of possible actions:
- `reverse` (reverses each sequence)
- `transcribe` (transcribes each sequence)
- `complement` (creates a complement sequence for each input sequence)
- `reverse_complement` (creates a reversed complement sequence for each input sequence)
- `check_ecor1_site` (can tell a user, has a sequence EcorI restriction site(s) or not)
- `count_dna_melting` (calculates the melting temperature of each sequence)
- `count_gc_content` (calculates GC-content of each sequence)

For `protein_tools`:
Provide a tool with the sequence(s) of the protein(s) in 1-letter format (for example, DYKDDDDK) and the function needed. Here is the catalogue of actions the user can choose: 
- count_length: gives the length(s) of the protein sequence(s)  
- count_nucleotide_length: counts the length(s) of the coding nucleotide sequence(s) of the protein sequence(s)

Function `filter_fastq` filters fastq sequences, given as a fastq file and returns a new fastq file with filtered sequences. The user provides the script with unput file path and optionally can give an output file name (default name is the same as input file has). The output file would be saved in a new direction with the name 'fastq_filtrator_results'. The filtrations occurs using GC-content boundaries, length boundaries and quality threshold. The user should provide function with these values. For GC-content and length boundaries you can type two numbers: lower and upper limits. The filters delete values that are beyound th boundaries (for example, GC-content boundaries from 40 to 80 mean that akk sequences with GC-content higer or lower will be filtered; the sequences with 40% GC-content or 80% Gc-content will be saved). Default number are: (0, 100) for GC-content, (0, 2**32) for length bondaries and 0 for quality threshold.

For `bio_files_processor.py`:
The user provides the script with input file path and output file name (default name is the same as input file has + '_2'). This tool can convert multiline sequence in one line sequence and can change position of a nucleotide. For changing position the user should also provide the script with the number of the nucleotide (the number can be negative, for example, -1).   

## Examples: 
Examples for `protein_tools` functions:  
```
function = 'count_aa_length'
prot1 = 'DYKDDDDK'
prot2 = 'DYKDDdDk'
```
The result would be:
```
[8, 8]
```
Almost same result will be obtained when using 'count_nucl_length'

Some examples for `run_dna_rna_tools`:
```
sequence = 'AGcgt'
function = 'check_ecor1_site'
```
The result:
```
False
```
```
sequence = 'AGcgt'
function = 'reverse'
```
The result:
```
'tgcGA'
```
As you can see, the programm saves the letters case.

## Troubleshooting
If the user sees ValueError when using run_dna_rna_tools, the user may inputted a non-protein sequence. The programm works with DNA sequences. Please, check the sequence. If the user sees ValueError when using my_first_bioinf_package.py tool and bio_files_processor.py, the user shoul check the existance of an input file path.

## Additional information
Accurate working of this code is not guaranteed (as usual), bur the author has done her best (also as usual). 

## Green is calming
![DSC00562](https://github.com/Zoea1/HW5_my_first_bioinf_package/assets/143959084/310af78f-24c1-41b2-8f0b-42b35c8b6446)
