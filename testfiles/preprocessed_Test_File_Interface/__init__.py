def __init__(self):
    self.blocks_written = 0
    self.blocks_read = 0
        self.blocks_replaced = 0

    self.number_of_seeks = 0
    self.total_seek_length_blocks = 0
    self.outfile = None
    self.infile = None
    self.isopen_read = False
    self.isopen_write = False
        self.directory_block_offset = 0

