import argparse
import os
from main import convert_syntax

def convert_nython_to_python(filepath, outputname=None):
    convert_syntax(filepath=filepath,outputname=outputname)
    

def main():
    parser = argparse.ArgumentParser(description='Convert Nython files to Python.')
    parser.add_argument('filepath', type=str, help='Path to the Nython file to convert.')
    parser.add_argument('-o', '--output', type=str, help='Output file name. If not specified, the input file name with .py extension is used.')
    args = parser.parse_args()

    convert_nython_to_python(args.filepath, args.output)

if __name__ == '__main__':
    main()
