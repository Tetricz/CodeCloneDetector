from utils.hash_file_compare import HashFileCompare
from utils.similarity_table import similarity_table
                
import sys

def hash_comp_from_input_list(input_list_file_name):
    # Read list of files to hash
    input_list_file = open(input_list_file_name, 'r')
    input_list = [line.rstrip('\n') for line in input_list_file]
    
    # Load the input files as a HashFileCompare and return it
    return HashFileCompare(input_list) 
                
def main():
    # Check argument usage
    if len(sys.argv) < 2:
        print("Usage: tlsh_evaluation.py testfiles/input_file_list.txt")
        exit(1)

    # Read list of files to hash
    hash_comp = hash_comp_from_input_list(sys.argv[1])
    
    s_table = similarity_table(hash_comp)
    
    # Report their inter-file similarity scores
    for file_name in s_table:
        print(f"\nHash similarities to {file_name}:")
        
        similarity_line = s_table[file_name]
        
        for score in similarity_line:
            print(f"{score[0]}\t{score[1]}")
    
    
if __name__ == '__main__':
    main()