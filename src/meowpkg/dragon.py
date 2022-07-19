#!/usr/bin/env python3
#
# Print a phase with a dragon

import argparse
import cowsay

def main():
    parser = argparse.ArgumentParser(description='Simple usage of cowsay module')
    parser.add_argument('message', default='Hello World!', help='Some message to show')

    args = parser.parse_args()

    cowsay.dragon(args.message)
