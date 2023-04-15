def write_dummy(self,buffer):
    self.outfile.write(buffer)
    self.blocks_written += 1
