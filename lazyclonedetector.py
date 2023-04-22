import sys
import os
import platform

from utils.preprocessor import preprocessor
from utils.hash_file_compare import HashFileCompare
from utils.tokenizer import tokenizer

file_seperation_char = "\\"

def build_paths_to_targets(target_dir):
    
    path_list = []

    cwd = os.getcwd()
    print(" running in: ",cwd)
    base_path = cwd + "/" + target_dir
    
    dirlist = os.listdir(base_path)

    for ob in dirlist:
        d = os.path.join(base_path, ob)
        if os.path.isdir(d):
            print(d)
            isin = d.find("preprocessed_")
            if isin >= 0:
                flist = os.listdir(d)
                for f in flist:
                    full_path = os.path.join(d, f)
                    if os.path.isfile(os.path.join(d, f)):
                        #print("      file:   ",f)
                        ispy = f.find(".py")
                        
                        if ispy > 0:
                             if (len(f) - ispy) == 3:  # it must end in .py, not just contain it
                                full_path = os.path.join(d, f)
                                #print("adding to list: ", full_path)
                                path_list.append(full_path)

    return path_list

def report_similarities(input_list,threshold):

    hfc = HashFileCompare(input_list)

    # Report their inter-file similarity scores
    for file_name in input_list:
        similarities = hfc.hash_value_similarities(file_name)
        
        key_function = lambda x: x[0]
        similarities = sorted(similarities, key=key_function, reverse=True)
        
        print(f"\nHash similarities to {file_name}:")
        
        for s in similarities:
            if s[0] > threshold:
                print(f"{s[0]}\t{s[1]}")

def tokenize_files_in_list(input_list):

    tokenized_files = []

    tkz = tokenizer()

    for name in input_list:

        ndx = name.rfind("\\")
        
        file_path = name[0:ndx]
        filename = name[ndx+1:len(name)]
        #print (" filename ",filename)

        tk = tkz.tokenize_python(file_path,filename)
        tkname = file_path + "/" + tk
        #print(" ------------> tkname: ",tkname)
        tokenized_files.append(tkname)
    
    return tokenized_files


def main(target_dir):

    prp = preprocessor()

    prp.process_dir(target_dir)

    input_list = build_paths_to_targets(target_dir)
    print("\n    Generated path list:")
    for l in input_list:
        print(" *  ",l)
    
    report_similarities(input_list, .5)

    tokenized_file_list = tokenize_files_in_list(input_list)
    #for name in tokenized_file_list:
    #   print(name)

    
    print("*********************************************************************")
    print("* After tokenization....")

    report_similarities(tokenized_file_list, .5)

    

if __name__ == "__main__":
    print(" argv: ",sys.argv)
    nargs = len(sys.argv)
    if (nargs < 2):
        print(" Usage: lazyclonedetector {foldername}")
        exit()
    directory = sys.argv[1]

    print(" OS is ",os.name)
    print(" plataform: ",platform.platform())
    running_on = platform.platform()
    if running_on.find("windows") < 0:
        file_seperation_char = "/"

    main(directory)
