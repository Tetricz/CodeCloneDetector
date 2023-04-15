import sys
import os
import io

import importlib.machinery
import importlib.util
import inspect

class preprocessor():
    def __init__(self):
        self.files_created = 0
        self.base_path = ""
 #------------------------------------------------------------------------------------   
 # this function removes two white spaces in a row
    def cleanup_line(self, line):
        ln = len(line)
        ndxnw = ln - len(line.lstrip()) # first non blank
        done = False
        while not done:

            dbblank = line.find("  ",ndxnw,ln)
            if dbblank < 0:
                done = True
            else:
                lfirst = line[0:dbblank]
                lsecond = line[dbblank+1:ln]
                line = lfirst + lsecond
        return line

#------------------------------------------------------------------------------------   
    def clean_function_body(self, buff, outfile, indent):

        for rline in buff:
        
            if len(rline) > 0:
                #print(" next line ----", rline)
                # remove trailing white space also removes newline
                line = rline.rstrip()

                ndxcom = line.find("#")
                if ndxcom >= 0:
                    retline = self.process_comment_line(line,ndxcom)
                    if len(retline) > 1:
                        outfile.write(retline+"\n")     # something left to write
                    continue
            
                # check for line of whitespaces
                if len(line.lstrip()) < 1:
                    continue
                # little more clean up - remove two white spaces in a row
                line = self.cleanup_line(line)
                if indent > 0:
                    outline = line[indent:len(line)] + "\n"
                else:
                    outline = line + "\n"

                outfile.write(outline)    



#------------------------------------------------------------------------------------
    
    def process_comment_line(self, line, ndxcom):
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
            retstr = line[0:ndxcom].rstrip() + "\n"
            return retstr
#-----------------------------------------------------------------------------------
    def process_inline_function(self, function_text, path, ismain):
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
                retline = self.process_comment_line(line,ndxcom)
                if len(retline) > 1:
                    outfile.write(retline)
        
        self.clean_function_body(buff, outfile, 0)
        

        outfile.close()

        #-----------------------------------------------------------------------------------
    def process_class_function(self, class_name, function_text, path, newpath):
        class_function_path  = path + "/"
        print("Class function path: ",class_function_path)
        buff = io.StringIO(function_text)
        line = buff.readline()

        index = line.find("(")
        # find indent amount
        indnt = line.find("def ")
        print(" first non blank char is in col: ", indnt)
        newstring = line[indnt:len(line)]
        
      
        funct_name = newstring[indnt:index-indnt]
        print(" function name: ",funct_name)
        #file1 = newpath + class_name + "_" + funct_name + ".py"
        file1 = newpath + "/" + funct_name + ".py"
        print(" Opening file: ",file1)
        try:
            outfile = open(file1, 'w')
        except IOError:
            print("could not open ",file1)
            exit()

        
        # write first line
        outfile.write(newstring)
            
        self.clean_function_body(buff, outfile, indnt)
        
        outfile.close()
#------------------------------------------------------------------------------------
    def process_class(self,file_in,newpath):
        full_file_path = self.base_path + "/" + file_in
        print(" full file path: ",full_file_path)
        loader = importlib.machinery.SourceFileLoader(file_in, full_file_path)

        mod = loader.load_module()

        for oname, oobj in inspect.getmembers(mod):
            if inspect.isfunction(oobj):
                print("   - Found function: ",oname)
            elif inspect.isclass(oobj):
                print("   - Found class: ",oname)
                classname = oname
                for mname, mobj in inspect.getmembers(oobj):
                    if inspect.isfunction(mobj):
                        print(" class contains function",mname)
                        src = inspect.getsource(mobj)
                        #print(src)
                        self.process_class_function(classname, src, full_file_path, newpath)
#----------------------------------------------------------------------------------
    def preprocess_python_file(self, current_path, file_in):

        # create a folder to store pre-processed code
        #cwd = os.getcwd()
        #print(" running in: ",cwd)
        index = file_in.find(".py")
        #print(" index: ", index)
        filename = "preprocessed_" + file_in[0:index:1]
        newpath = self.base_path + "/" + filename
    
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

         # check to see if contains a class
        ic = original_file_text.find("class ")
        if ic >= 0:
            self.process_class(file_in, newpath)
            return original_file_text
        else:
            text_to_process = original_file_text

            # splits into functions , split on "def"
            #print(original_file_text)
            funs = text_to_process.split("def ")
            print(" length of funs: ",len(funs))
            if len(funs) == 1:
                ismain = True
            else:
                ismain = False
            print("+++++++++++++++++++++++++++++++++++++++++")
            for s in funs:
                print("length of element: ",len(s))
                if (len(s) > 2):
                    self.process_inline_function(s, newpath, ismain)
                    print(" -------------------")

        return original_file_text

    #------------------------------------------------------------------------------
    def process_dir(self, target_dir):

        cwd = os.getcwd()
        print(" running in: ",cwd)
        self.base_path = cwd + "/" + target_dir

        dirlist = os.listdir(self.base_path)
        for file_in in dirlist:
            split_txt  = os.path.splitext(file_in)
            
            if (split_txt[1] == ".py"):
                print(" base: ",split_txt[0]," extension = ",split_txt[1])
                filetext1 = self.preprocess_python_file(self.base_path, file_in)
    
