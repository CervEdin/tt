#!/bin/env python3

import argparse
import sys
import tiktoken


def main():
    parser = argparse.ArgumentParser()
    # Support either encode or decode, defualt to encode
    parser.add_argument("-d", "--decode",
                        action="store_true",
                        help="Decode tokens (instead of enocding strings)")
    # Support specifying specific encoding, default to cl100k_base
    parser.add_argument("-e", "--encoding",
                        type=str,
                        default="cl100k_base",
                        help="Encoding to use (default: cl100k_base)")
    parser.add_argument("file",
                        nargs='?', type=str, default='-',
                        help="Input file (default: stdin)")
    args = parser.parse_args()
    enc = tiktoken.get_encoding(args.encoding)

    with open(args.file, 'r') if args.file != '-' else sys.stdin as f:
        if not args.decode:
            tokens = enc.encode(''.join((l for l in f)))
            print(' '.join(( str(x) for x in tokens)))
        else:
            tokens = enc.decode([
                int(w)
                for l in f
                for w in l.split()
                ])
            print(''.join(str(x) for x in tokens))


if __name__ == "__main__":
    main()
