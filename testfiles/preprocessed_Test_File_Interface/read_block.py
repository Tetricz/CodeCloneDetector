def read_block(self):
    try:
        buffer = self.infile.read(self.BLOCKSIZE)
    except IOError:
            print(" could not read from file")

    self.blocks_read += 1
    return buffer
