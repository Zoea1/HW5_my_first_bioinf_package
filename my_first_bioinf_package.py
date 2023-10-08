from inner_code import filter_gc_content, filter_length, filter_quality
from typing import Tuple, Union
def filter_fastq (seqs: dict, length_bounds: Union [tuple, int] =(0, 2**32), gc_bounds: Union [tuple, int] =(0, 100), quality_threshold: int=0) -> dict: 
    """  
    Returns filtered sequences\n 
    Arguments:\n
    seqs (dict) - the dictionary with the sequences that should be filtered;\n
    gc_bounds (tuple or int) - the boundaries for gc-content; default meaning - (0; 100);\n  
    length_bounds (tuple or int) - the boundaries for length; default meaning - (0, 2**32);\n
    quality_threshold (int) - the number for quality threshold; default meaning - 0\n
    Return:\n
    dict - filtered sequences, collected in a dictionary  
    """
    for key, value in seqs.items():
        bad_keys1 = filter_gc_content(gc_bounds, key, value)
        bad_keys2 = filter_length(length_bounds, key, value)
        bad_keys3 = filter_quality(quality_threshold, key, value)
    for key in bad_keys1 or bad_keys2 or bad_keys3:
        del seqs[key]

from inner_code import count_aa_length, count_nucl_length
def protein_tools (function : str, *prots : str) -> (int): 
    """
    Consists of several functions, is able to:\n
      -count the length of the sequence\n
      -count the length of the coding nucleotide sequence of the inputted sequence\n
     Arguments:\n
      -function (str) - the name of the action, the user wants to do on the sequence(s)\n
      -prots (str) - the sequence(s) that should be manipulated\n
     Return:\n
      -int - results of counts

    """
    functions = {'count_length':count_aa_length, 'count_nucleotide_length':count_nucl_length}
    protein = []
    for prot in prots:
        protein.append(functions[function](prot))
    if len(protein) == 1:
        return protein[0]
    else:
        return protein
    

from inner_code import is_dna, check_ecor1_site, count_gc_content, count_dna_melting, reverse, transcribe, complement, reverse_complement
def run_dna_rna_tools(*inputs:str) -> Union [str, bool]: 
    """
    Operates on DNA sequences, can transcribe, reverse, give a complement or reverse complement sequences, check EcoRI site(s),
    count GC-content and melting temperature.\n
    Arguments:\n
    sequences (str) - sequences to be operated\n
    function - the name of a function to be done\n
    Return:\n
    bool - when checking EcoRI site\n
    str - other operations
    """ 
    sequences = inputs[:-1]
    function = inputs[-1]
    functions = {'check_ecor1_site':check_ecor1_site, 'count_gc_content':count_gc_content, 
                 'count_dna_melting':count_dna_melting, 'reverse':reverse,
                 'transcribe':transcribe,'complement':complement,
                 'reverse_complement':reverse_complement}
    dna_sequences = []
    for sequence in sequences:  
        is_dna(sequence)
        dna_sequences.append(functions[function](sequence))
    if len(dna_sequences) == 1:
        return dna_sequences[0]
    else:
        return dna_sequences
