def read_required_block(self,blocknum):
        file_offset = (self.directory_block_offset + blocknum) * self.BLOCKSIZE

    self.infile.seek(file_offset,0)
    self.number_of_seeks += 1
        self.total_seek_length_blocks += file_offset

    buffer = self.infile.read(4096)
    return buffer
