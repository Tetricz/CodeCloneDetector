def open_for_write(self,filename):
    print(" Opening file: ",filename,)
    try:
        self.outfile = open(filename, 'wb')
    except IOError:
        error_print(f"could not open {filename}")
    self.isopen_write = True
    self.blocks_written = 0
