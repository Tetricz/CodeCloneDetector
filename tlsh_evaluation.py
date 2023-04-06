# Locality sensitive hashing
import tlsh

# String similarity
from fuzzywuzzy import fuzz

# Encoding for converting strings to bytes
encoding = 'utf-8'

# List of example files
file_list = [
    'testfiles/check_polygon.py',
    'testfiles/check_polygon2.py',
    'testfiles/testplot.py',
    'testfiles/testplot2.py'
]

def hash_and_add_to_list(hash_list, text, text_id):
    hash_value = tlsh.hash(bytes(text, encoding))
    hash_list += [(hash_value, text_id)]

def hash_list_from_file_list(file_list):
    hash_list = []
    
    for file_name in file_list:
        # Read whole file. This will be replaced by individual function blocks.
        text = open(file_name, 'r').read()
        
        # Hash and add to the list
        hash_and_add_to_list(hash_list, text, file_name)
    
    return hash_list
    
def hash_value_similarities(hash_item, hash_list):
    return [(fuzz.ratio(hash_item[0], other_hash_item[0]) / 100,
             other_hash_item[1])
                for other_hash_item in hash_list]
    
def main():    
    hash_list = hash_list_from_file_list(file_list)
    
    '''Similar but slightly different files have similar but 
        slightly different hash values. However, the differences
        in the hash values can occur anywhere in the hash.
        
        So we need to calculate similarities of each hash value 
        to other hash values independently with ref to each hash value.'''
        
    for hash_item in hash_list:
        hash_list_excluding_current = [x for x in hash_list if x is not hash_item]
        similarities = hash_value_similarities(hash_item, hash_list_excluding_current)
        
        key_function = lambda x: x[0]
        similarities = sorted(similarities, key=key_function, reverse=True)
        
        most_similar = similarities[0]
        
        print(f"The most similar file to {hash_item[1]} is {most_similar[1]} with a score of {most_similar[0]}")
    
    
if __name__ == '__main__':
    main()