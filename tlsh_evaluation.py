from utils.hash_compare import hash_comp_from_input_list
from utils.similarity_table import similarity_table
                
import sys
                
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