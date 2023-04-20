# Locality sensitive hashing
import tlsh

# String similarity
from fuzzywuzzy import fuzz

class HashFileCompare:
    ''' Read the files specified in a list of filenames, hash them, 
        and store the hashes with the filenames.
    '''
    def __init__(self, file_list):
        self.hash_list = []
        
        for file_name in file_list:
            text = open(file_name, 'r').read()
        
            hash_value = tlsh.hash(bytes(text, 'utf_8'))
            self.hash_list += [(hash_value, file_name)]
    
    ''' Compute string similarity scores between one hash and the rest of the hashes.
    '''
    def hash_value_similarities(self, file_name):
        hash_item = [x for x in self.hash_list if x[1] is file_name][0]
        hash_list_minus = [x for x in self.hash_list if x[1] is not file_name]
    
        return [(fuzz.ratio(hash_item[0], other_hash_item[0]) / 100,
                    other_hash_item[1])
                for other_hash_item in hash_list_minus]
    
    ''' Return the list of files which have hashes stored.
    '''
    def get_file_list(self):
        return [hash_item[1] for hash_item in self.hash_list]
