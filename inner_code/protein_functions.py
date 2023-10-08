def count_aa_length (arg: str) -> int:  
    """ 
    Counts the length of the sequence\n
    Arguments:\n
    arg (str) - the sequence, which length should be counted\n
    Return:\n
    int - the result of the count
    """
    return len (arg)


def count_nucl_length (arg: str) -> int: 
    """
    Counts the length of the nucleotide sequence that codes the inputted aminoacid sequence\n
    Arguments:\n
    arg (str) - the sequence, which coding nucleotide sequence length should be counted\n
    Return:\n
    int - the result of the count
    """
    return len (arg) * 3