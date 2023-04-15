def open_for_read(self,filename):
    print(" Opening file: ",filename,)
    try:
        self.infile = open(filename, 'rb')
    except IOError:
        error_print(f"could not open {filename}")
    self.isopen_read = True
