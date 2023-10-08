from typing import Tuple, Union
def filter_gc_content(gc_bounds: Union [tuple, int], key: str, value: Union [tuple, int]):
    """
    Filters sequences asccording to GC-content\n
    Arguments:\n
    gc_bounds (tuple, int) - desired boundaries for GC-content. Default boundaries - (0, 100)\n
    key - key from main function dictionary\n
    value - value from main function dictionary\n
    Return:\n
    bad_keys - a list with inappropriate sequences
    """  
    bad_keys1 = []
    if len(gc_bounds) == 1:
        gc_bounds.append(0)
        gc_bounds.sort()
    gc_count = 0
    for i in value[0]:
        if(i == 'G' or i == 'C'):  
            gc_count += 1
    gc_content = round(((gc_count/len(value[0])) * 100), 2)
    if gc_bounds[0] > gc_content or gc_content > gc_bounds[-1]:  
        bad_keys1.append(key)
    return bad_keys1


def filter_length(length_bounds: Union [tuple, int], key: str, value: Union [tuple, int]) -> list:  
    """
    Filters sequences asccording to sequences length\n
    Arguments:\n
    length_bounds (tuple, int) - desired boundaries for length. Default boundaries - (0, 2**32)\n
    key - key from main function dictionary\n
    value - value from main function dictionary\n
    Return:\n
    bad_keys - a list with inappropriate sequences
    """ 
    bad_keys2 = []
    if len(length_bounds) == 1:
        length_bounds.append(0)
        length_bounds.sort()
    if len(value[0]) < length_bounds[0] or len(value[0]) > length_bounds[-1]: 
        bad_keys2.append(key)
    return bad_keys2


def filter_quality(quality_threshold: int, key: str, value: Union [tuple, int]):  
    """
    Filters sequences asccording to the quality\n
    Arguments:\n
    quality_threshold (int) - desired threshold for quality. Default number - 0\n
    key - key from main function dictionary\n
    value - value from main function dictionary\n
    Return:\n
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