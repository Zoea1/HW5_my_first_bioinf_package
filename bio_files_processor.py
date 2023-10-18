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
        output_fasta_2 = os.path.basename(input_fasta)
    elif output_fasta.find('.fasta') == False:
        output_fasta_2 = output_fasta + '.fasta'
    else:
        output_fasta_2 = output_fasta
    with open(os.path.join(output_dir, output_fasta_2), mode = 'w') as file:
        file.write(sequence)
        

            



