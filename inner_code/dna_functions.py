def check_ecor1_site(sequence:str) -> bool:
    """
    Checks the presence of EcoRI site(s) in a sequence
    Arguments:
    sequence (str) - the sequence where is needed to find EcoRI
    Return:
    bool
    """
    sequence_lower = sequence.lower()
    if (sequence_lower.find('gaatc') == -1):
        return True        
    else:
        return False


def count_gc_content(sequence:str) -> str:
    """
    Counts GC-content of the sequence
    Arguments:
    sequence (str) - the sequence, the GC-content of which should be counted
    Return:
    str - a sentence with the GC-content amount
    """  
    sequence_lower = sequence.lower()
    gc_count = 0
    for nucleotide in sequence_lower:  
        if nucleotide == 'g' or nucleotide == 'c':  
          gc_count += 1
    gc = round(((gc_count / len(sequence_lower))*100), 2)
    print('The GC-content of the sequence', sequence,  'is', gc, '%')


def count_dna_melting(sequence:str) -> str:
    """
    Counts DNA melting temperature
    Arguments:
    sequence (str) - the sequence, the melting temperature of which should be counted
    Return:
    str - a sentence with the melting temperature
    """  
    sequence_lower = sequence.lower()
    gc_count = 0
    at_count = 0
    for nucleotide in sequence_lower:
      if nucleotide == 'g' or nucleotide == 'c':  
        gc_count += 1
      elif nucleotide == 't' or nucleotide == 'a':
        at_count += 1
    melting_t = 2 * at_count + 4 * gc_count
    print('Melting temperature of the sequence', sequence, 'is', melting_t, 'degrees')


def is_dna(sequence:str) -> None:
    """
    Checks whether the sequence is a DNA sequence or not
    Arguments:
    sequence (str) - a sequence to be checked
    Return:
    None
    """
    sequence_lower = sequence.lower()
    for i in range (len(sequence_lower)):
        if ((sequence_lower[i] == 'c') or (sequence_lower[i] == 'g') or (sequence_lower[i] == 't') or (sequence_lower[i] =='a')):
            continue
        else:
            raise ValueError('It is not a DNA sequence!')
 

def reverse(sequence:str) -> str:
    """
    Reverses a sequence
    Arguments:
    sequence (str) - a sequence to be reversed
    Return:
    reversed sequence (str)

    """
    rev_seq = []
    rev_seq.append(sequence[::-1])
    return rev_seq


def transcribe(sequence:str) -> str:
    """
    Transcribes sequence
    Arguments:
    sequence (str) - a sequence to to be transcribed
    Return:
    transcribed sequence (str) 
    """
    transcribed_seq = []
    transcribed_seq.append(sequence.replace('T', 'U').replace('t', 'u'))
    return transcribed_seq


def complement(sequence:str) -> str:
    """
    Returns complement sequence
    Arguments:
    sequence (str) - a sequence, for which a complement should be created
    Return:
    complement (str) - a complement sequence
    """
    COMPLEMENT_DICTIONARY = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}
    complement_seq_result = []
    complement_seq = ''
    for i in sequence:
        complement_seq += COMPLEMENT_DICTIONARY.get(i)
    complement_seq_result.append(complement_seq)
    return complement_seq_result


def reverse_complement(sequence:str) -> str:
    """
    Returns reversed complement sequence
    Arguments:
    sequence (str) - a sequence, for which a reversed complement should be created
    Return:
    reversed complement (str) - a reversed complement sequence
    """
    COMPLEMENT_DICTIONARY = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}
    reverse_complement_seq_result = []
    complement_seq = ''
    rev_seq = reverse(sequence)
    for i in rev_seq:
        complement_seq += COMPLEMENT_DICTIONARY.get(i)
    reverse_complement_seq_result.append(complement_seq)
    return reverse_complement_seq_result

        
