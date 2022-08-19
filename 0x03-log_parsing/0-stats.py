#!/usr/bin/python3
"""Parses log from standard input"""
import sys


def parse_logs():
    """Parses log from stdin"""
    accept_codes = {
        200: 0, 301: 0,
        400: 0, 401: 0,
        403: 0, 404: 0,
        405: 0, 500: 0
        }
    try:
        line_num = 0
        file_size = 0
        # status_codes = {}
        for line in sys.stdin:
            line_num += 1
            tokens = line.split(" ")[-2:]
            file_size += int(tokens[1])
            code = tokens[0]
            if (code).isdigit() and int(code) in accept_codes.keys():
                accept_codes[int(code)] = accept_codes.get(int(code)) + 1
            keys = list(accept_codes.keys())
            # status_codes.sort()
            if line_num > 9:
                line_num = 0
                print("File size: {}".format(file_size))
                [print("{}: {}".format(i, accept_codes.get(i))) for i in keys
                    if accept_codes.get(i) > 0]
    except Exception as e:
        # [print("{}: {}".format(i, status_codes.get(i))) for i in keys]
        [print("{}: {}".format(i, accept_codes.get(i))) for i in keys
            if accept_codes.get(i) > 0]


if __name__ == "__main__":
    parse_logs()
