import re
import os


def main():
    count = 0
    chunk_size = 16
    size = os.path.getsize('hexDump.py')
    print(size)
    with open("hexDump.py", "rb") as file_bytes:
        for chunk in range(int(size/chunk_size)):
            count = read_bytes(count, file_bytes)
        read_bytes(count, file_bytes)
    return None


def read_bytes(count: int, file_object: file) -> int:
    """
    Returns count += 1
    Given a file_object, read 16 bytes from it, format the bytes,
    then print to terminal the current off_set, the bytes, and any
    printable values.
    """
    target_bytes = file_object.read(16) #Read 16 bytes from file 
    target_bytes = [ format(byte) for byte in target_bytes ] 
    
    target_print = ''
    for i in range(8):
        target_print += ' ' + ''.join(target_bytes[2*i : 2*i+2])
    if len(target_print) < 41:
        target_print += (41 - len(target_print)) * ' '

    value_bytes = [ byte_value(byte) for byte in target_bytes ]
    value_print = ''.join(value_bytes)

    print_count = ('0' * (8 - len(hex(count)))) + hex(count)[2:] + '0'

    print(print_count, target_print, value_print)

    count += 1

    return count


def format(byte):
    if len(hex(byte)) == 3:
        ret_val = '0' + hex(byte)[2:]
    else:
        ret_val = hex(byte)[2:]
    return ret_val


def byte_value(byte):
    try:
        if chr(int(byte, 16)) != '\n':
            return '' + chr(int(byte, 16))
        else:
            return ' '
    except:
        return ' '

    
if __name__ == "__main__":
    main()
