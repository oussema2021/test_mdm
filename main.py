from SparseArray import SparseArray
import sys
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('querie', help='set the querie argument',type=str)
    args = parser.parse_args()

    strings = os.environ.get("STRINGS")
    
    cv = SparseArray(list(strings.split(',')))
    r =cv.matchingStrings(args.querie.split(','))
    print(r)
