import os
def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None):
    """
    Converts sequence in fasta file in one line sequence in a new fasta file.
    Arguments: 
    input_fasta (str) - a path to a fasta file which should be converted
    output_fasta - a name for a new converted fasta file
    Return:
    a fasta file with sequence written in one line
    """
    sequence = []
    if os.path.isfile(input_fasta) == False:
        raise ValueError ('The path does not exist!')
    with open(os.path.join(input_fasta)) as file:
        for line in file:
            if not line.startswith('>'):
                line = line.strip()
                sequence = ''.join(sequence.append(line))
    output_dir = os.path.dirname(input_fasta)
    if output_fasta == None:
        input_fasta2 = os.path.basename(input_fasta) + '_2'
        output_fasta_2 = os.path.basename(input_fasta2)
    elif output_fasta.find('.fasta') == False:
        output_fasta_2 = output_fasta + '.fasta'
    else:
        output_fasta_2 = output_fasta
    with open(os.path.join(output_dir, output_fasta_2), mode = 'w') as file:
        file.write(sequence)
    
import os
def change_fasta_start_pos(input_fasta: str, shift: int, output_fasta: str = None):
    """
    Arguments: 
    input_fasta (str) - a path to a fasta file which should be shifted
    shift - the index of nucleotide (indexing begins with 0) that should be moved on the first place
    output_fasta - a name for a new fasta file with shifted sequence
    Return:
    a fasta file with shifted sequence
    """
    if os.path.isfile(input_fasta) == False:
        raise ValueError ('The path does not exist!')
    with open(os.path.join(input_fasta)) as file:
        if not line.startswith('>'):
            line = line
            if shift > 0:
                first_part_line = line[:shift]
                last_part_line = line[shift+1:]
                shifting_nucleotide = line[shift]
                result_sequence = shifting_nucleotide + first_part_line + last_part_line 
            elif shift == -1:
                shifting_nucleotide = line[shift]
                first_part_line = line[:shift]
                result_sequence = shifting_nucleotide + first_part_line
            return result_sequence
    output_dir = os.path.dirname(input_fasta)
    if output_fasta == None:
        input_fasta2 = os.path.basename(input_fasta) + '_2'
        output_fasta_2 = os.path.basename(input_fasta2)
    elif output_fasta.find('.fasta') == False:
        output_fasta_2 = output_fasta + '.fasta'
    else:
        output_fasta_2 = output_fasta
    with open(os.path.join(output_dir, output_fasta_2), mode = 'w') as file:
        file.write(result_sequence)    

            



