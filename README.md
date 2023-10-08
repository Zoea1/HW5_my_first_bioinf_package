# HW5_my_first_bioinf_package
This is my_first_bioinf_package.py tool. This tool is able to work with protein sequences and DNA sequences. It imports functions from inner_code folder. 
# Installation
Download my_first_bioinf_package.py and inner_code folder. You can use this code in your programms. This script cannot work independently, because there is no input from keyboard. 
# Usage
First, a user should chose what kind of operation he or she wants to do. There are three main options in the package:
- filter fastq sequences (use `filter_fastq` function) 
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

Function `filter_fastq` filters fastq sequences, given as a dictionary with a sequence name as a key and a sequence itself and its quality as a value, and returns a new filtered dictionary with fastq sequences. The filtrations occurs using GC-content boundaries, length boundaries and quality threshold. The user should provide function with these values. For GC-content and length boundaries you can type two numbers: lower and upper limits. The filters delete values that are beyound th boundaries (for example, GC-content boundaries from 40 to 80 mean that akk sequences with GC-content higer or lower will be filtered; the sequences with 40% GC-content or 80% Gc-content will be saved). Default number are: (0, 100) for GC-content, (0, 2**32) for length bondaries and 0 for quality threshold.

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
sequence = 'AGcgt'
function = 'reverse'
```
The result:
```
'tgcGA'
```
As you can see, the programm saves the letters case.

Example of inputs for `filter_fastq`:
```
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD')}
```

## Troubleshooting
If the user sees ValueError when using run_dna_rna_tools, the user may inputted a non-protein sequence. The programm works with DNA sequences. Please, check the sequence.

## Additional information
Accurate working of this code is not guaranteed, bur the author has done her best. 

