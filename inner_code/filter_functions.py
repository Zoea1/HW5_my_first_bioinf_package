from typing import Tuple, Union
def filter_gc_content(gc_bounds: Union [tuple, int], key: str, value: Union [tuple, str]):
    """
    Filters sequences asccording to GC-content
    Arguments:
    gc_bounds (tuple, int) - desired boundaries for GC-content. Default boundaries - (0, 100)
    key - key from main function dictionary
    value - value from main function dictionary
    Return:
    bad_keys - a list with inappropriate sequences
    """  
    bad_keys1 = []
    if isinstance(gc_bounds, int) or isinstance(gc_bounds, float):
        gc_bounds = (0, gc_bounds)
    gc_count = 0
    for i in value[0]:
        if(i == 'G' or i == 'C'):  
            gc_count += 1
    gc_content = round(((gc_count / len(value[0])) * 100), 2)
    if gc_bounds[0] > gc_content or gc_content > gc_bounds[-1]:    
        bad_keys1.append(key)
    return bad_keys1


def filter_length(length_bounds: Union [tuple, int], key: str, value: Union [tuple, str]) -> list:  
    """
    Filters sequences asccording to sequences length
    Arguments:
    length_bounds (tuple, int) - desired boundaries for length. Default boundaries - (0, 2**32)
    key - key from main function dictionary
    value - value from main function dictionary
    Return:
    bad_keys - a list with inappropriate sequences
    """ 
    bad_keys2 = []
    if isinstance(length_bounds, int) or isinstance(length_bounds, float):
        length_bounds = (0, length_bounds)
    if len(value[0]) < length_bounds[0] or len(value[0]) > length_bounds[-1]:
        bad_keys2.append(key)
    return bad_keys2


def filter_quality(quality_threshold: int, key: str, value: Union [tuple, str]):
    """
    Filters sequences asccording to the quality
    Arguments:
    quality_threshold (int) - desired threshold for quality. Default number - 0
    key - key from main function dictionary
    value - value from main function dictionary
    Return:
    bad_keys - a list with inappropriate sequences
    """
    bad_keys3 = []
    quality_count = 0
    mean_quality = 0
    for i in value[-1]:
        quality_count += ord(i)
    mean_quality = quality_count / len(value[-1])
    if mean_quality < quality_threshold:
        bad_keys3.append(key)
    return bad_keys3


import os
def turn_into_dict(input_path: str) -> dict:
    """
    Turns a fastq file into a dictionary that can be processed further
    Arguments:
    input_path (str) - the path of the fastq file with the sequences that should be filtered;
    Return:
    dictionary 
    """
    seqs = dict()
    name = []
    sequence = []
    comment = []
    quality = []
    if os.path.isfile(input_path) == False:
        raise ValueError ('The path does not exist!')
    with open(os.path.join(input_path)) as file: 
        for i in file:
            name.append(file.readline())
            if name[i] != '':
                sequence.append(file.readline())
                comment.append(file.readline())
                quality.append(file.readline())
    for i in range (len(sequence)):
        seqs[name[i]] = (sequence[i], comment[i], quality[i])
    return seqs


import os
def turn_into_fastq(seqs: dict, input_path: str, output_filename: str = None):
    """
    Turns a dictionary into a fastq file that will be saved
    Arguments:
    input_path (str) - the path of the fastq file with the sequences that should be filtered;
    output_filename - 
    Return:
    output_filename file - filtered sequences, collected in a fastq file with the name chosen by a user (default name - as the name of the unfiltered file)
    """
    output_dir = 'fastq_filtrator_results'
    if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)
    if type(output_filename) == None:
        filename = os.path.basename(input_path)
    else:
        filename = output_filename
    with open(os.path.join(output_dir, filename), mode = 'w') as file:
        for key, value in seqs:
            file.write(key + '\n')
            file.write(value[0] + '\n')
            file.write(value[1] + '\n')
            file.write(value[2] + '\n')
    
