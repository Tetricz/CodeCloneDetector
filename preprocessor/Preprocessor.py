import sys
import os
import io

def process_comment_line(line, ndxcom):
    # if the line has text before the comment that must be preserved we return it
    # otherwise we return an empty string and nothing is written
    if ndxcom == 0:
        #print(" this line is all comment: ",line)
        return "\n"
    if ndxcom > 0:
        # find first non whitespace
        ndxnw = len(line) - len(line.lstrip())
        if ndxcom == ndxnw:     # comment is the first non-whitespace
            #print(" this line is all comment: ",line)
            return "\n"
        retstr = line[0:ndxcom] + "\n"
        return retstr
#------------------------------------------------------------------------------
def process_function(function_text, path, ismain):
    buff = io.StringIO(function_text)
    line = buff.readline()
    #print("line: ",line)
    isfunction = False
    if ismain:
        fname = "file__main"
    else:
        index = line.find("(")
        isfunction = False
        if (index > 1):  
            isfunction = True
            fname = line[0:index]
            #print(" function name: ",fname)
        # not a function 
        else:
            fname = "file_frontmater"

    file1 = path + "/" + fname + ".py"

    print(" Opening file: ",file1)
    try:
        outfile = open(file1, 'w')
    except IOError:
        print("could not open ",file1)
        exit()

    # now process that first line
    if isfunction:
        text = "def " + line
        outfile.write(text)
    else:
        #text = " # just some declarations before first function\n"
        #outfile.write(text)
        ndxcom = line.find("#")
        if (ndxcom >= 0):
            retline = process_comment_line(line,ndxcom)
            if len(retline) > 1:
                outfile.write(retline)
    for line in buff:
        
        if len(line) > 0:
            #print(" next line ----", line)
            ndxcom = line.find("#")
            if ndxcom >= 0:
                #print(" this line is all comment: ",line)
                retline = process_comment_line(line,ndxcom)
                if len(retline) > 1:
                    outfile.write(retline)     # something left to write
                continue
            
            # check for line of whitespaces
            if len(line.lstrip()) < 1:
                continue
            outfile.write(line)

    outfile.close()

#------------------------------------------------------------------------------
def preprocess_python_file(current_path, file_in):

    # create a folder to store pre-processed code
    #cwd = os.getcwd()
    #print(" running in: ",cwd)
    index = file_in.find(".py")
    #print(" index: ", index)
    filename = "proprocessed_" + file_in[0:index:1]
    newpath = current_path + "/" + filename
    
    file1 = current_path + "/" + file_in
    if not os.path.exists(newpath):
        print(" Creating directory ",newpath)
        os.makedirs(newpath)
    else:
        print(" Using directory ",newpath)

    # splits into functions , split on "def"
    
    print(" Opening file: ",file1)
    try:
        infile = open(file1, 'r')
    except IOError:
        print("could not open ",file1)
        exit()

    original_file_text = infile.read()
    #print(original_file_text)
    funs = original_file_text.split("def ")
    print(" length of funs: ",len(funs))
    if len(funs) == 1:
        ismain = True
    else:
        ismain = False
    print("+++++++++++++++++++++++++++++++++++++++++")
    for s in funs:
        print("length of element: ",len(s))
        if (len(s) > 2):
            process_function(s, newpath, ismain)
            print(" -------------------")

    return original_file_text

#------------------------------------------------------------------------------
def main(args):

    nargs = len(args)
    if (nargs < 2):
        print(" Usage: preproces {filename")
        exit()
    directory = args[1]
    cwd = os.getcwd()
    print(" running in: ",cwd)
    base_path = cwd + "/" + directory

    dirlist = os.listdir(base_path)
    for file_in in dirlist:
        split_txt  = os.path.splitext(file_in)
        print(" base: ",split_txt[0]," extension = ",split_txt[1])
        if (split_txt[1] == ".py"):
            filetext1 = preprocess_python_file(base_path, file_in)
    
    
if __name__ == "__main__":
    print(" argv: ",sys.argv)
    main(sys.argv)
