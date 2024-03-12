import struct

def encode_16bit_number(number: int) -> bytes:
    return struct.pack('!H', number)