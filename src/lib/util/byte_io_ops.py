# byte-IO operations
# ------------------------------------------------------------------------

""" write
"""

def write_int(fp, i, signed=True):
    """write an integer i to file by its file handle
    Return: current position after writing
    """
    fp.write(i.to_bytes(4,"little", signed=signed))
    return fp.tell()


def write_chr(fp, char):
    """write a char to file by its file handle
    Return: current position after writing
    """
    fp.write(char.encode('ascii'))
    return fp.tell()


def write_string(fp, s):
    """write a string s to file by its file handle
    Return: current position after writing
    """
    fp.write(s.encode('ascii'))
    return fp.tell()


""" read
"""

def read_int_at(fp, pos):
    """read an integer from file, return 
    """
    fp.seek(pos)
    return read_int(fp)

def read_int(fp, signed=True):
    """read an integer from file
    """
    return int.from_bytes(fp.read(4), byteorder='little', signed=signed)


def read_string(fp, sz):
    """read a string from file
    """
    return fp.read(sz).decode("ascii") 


def read_chr_at(fp, pos):
    """read a char from file
    """
    fp.seek(pos)
    return read_chr(fp)


def read_chr(fp):
    return fp.read(1).decode('ascii')
