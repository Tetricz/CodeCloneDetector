from utils.hash_file_compare import HashFileCompare
                
import sys
                
def main():
    # Read list of files to hash
    input_list_file_name = sys.argv[1]
    input_list_file = open(input_list_file_name, 'r')
    input_list = [line.rstrip('\n') for line in input_list_file]
    
    # Load the input files as a hash_file_compare
    hfc = HashFileCompare(input_list)
    
    # Report their inter-file similarity scores
    for file_name in input_list:
        similarities = hfc.hash_value_similarities(file_name)
        
        key_function = lambda x: x[0]
        similarities = sorted(similarities, key=key_function, reverse=True)
        
        print(f"\nHash similarities to {file_name}:")
        
        for s in similarities:
            print(f"{s[0]}\t{s[1]}")
    
    
if __name__ == '__main__':
    main()