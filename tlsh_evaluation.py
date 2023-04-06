import tlsh

# Encoding for converting strings to bytes
encoding = 'utf-8'

def hash_and_add_to_list(hash_list, text):
    hash_item = tlsh.hash(bytes(text, encoding))
    hash_list += [hash_item]

def hash_list_from_file_list(file_list):
    hash_list = []
    
    for file_name in file_list:
        # Read whole file. This will be replaced by individual function blocks.
        text = open(file_name, 'r').read()
        
        # Hash and add to the list
        hash_and_add_to_list(hash_list, text)
    
    return hash_list
    
def main():
    file_list = [
        'testfiles/check_polygon.py',
        'testfiles/check_polygon2.py',
        'testfiles/testplot.py',
        'testfiles/testplot2.py'
    ]
    
    hash_list = hash_list_from_file_list(file_list)
    
    hash_list = sorted(hash_list)
    
    hash_list
    
if __name__ == '__main__':
    main()