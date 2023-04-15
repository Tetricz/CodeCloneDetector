def close_file(self):
    if (self.isopen_write):
        self.outfile.close()
        self.isopen_write = False
        return self.blocks_written
    if (self.isopen_read):
        self.infile.close()
        self.isopen_read = False
    return 0
