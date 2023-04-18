from utils.hash_file_compare import HashFileCompare
                
import sys
                
def main():
    # Check argument usage
    if len(sys.argv) < 2:
        print("Usage: tlsh_evaluation.py testfiles/input_file_list.txt")
        exit(1)

    # Read list of files to hash
    input_list_file_name = sys.argv[1]
    input_list_file = open(input_list_file_name, 'r')
    input_list = [line.rstrip('\n') for line in input_list_file]
    
    # Load the input files as a HashFileCompare
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