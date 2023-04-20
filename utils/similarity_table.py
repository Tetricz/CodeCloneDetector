from utils.hash_file_compare import HashFileCompare

def sorted_similarities(hash_comp, file_name):
    similarities = hash_comp.hash_value_similarities(file_name)
    
    return sorted(similarities, key = (lambda x: x[0]), reverse = True)

def similarity_table(hash_comp):
    file_list = hash_comp.get_file_list()
    
    return {file_name: sorted_similarities(hash_comp, file_name) for file_name in file_list}