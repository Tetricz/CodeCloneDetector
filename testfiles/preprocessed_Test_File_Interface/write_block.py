def write_block(self,buffer):
    self.outfile.write(buffer)
    self.blocks_written += 1
