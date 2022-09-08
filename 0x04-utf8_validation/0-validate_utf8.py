#!/usr/bin/python3
"""
Defines  a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Returns True if data is a valid UTF-8 encoding
    Otherwise returns False
    First byte:
    '00000000' == 0 <> '01111111' == 127
    '11000000' == 192 <> '11011111' == 223
    '11100000' == 224 <> '11101111' == 239
    '11110000' == 240 <> '11110111' == 247

    Other bytes:
    '10000000' == 128 <> '10111111' == 191
    """

    length = len(data)

    if length == 0:
        return True

    val = data[0]
    if val > 255:
        return False
    if val < 128:
        return True
    elif (val >= 192) and (val <= 223):
        no_of_bytes = 2
    elif (val >= 224) and (val <= 239):
        no_of_bytes = 3
    elif (val >= 240) and (val <= 247):
        no_of_bytes = 4
    else:
        return False

    if length < no_of_bytes:
        return False

    for i in range(1, no_of_bytes):
        if not ((data[i] >= 128) and (data[i] <= 191)):
            return False

    return True
