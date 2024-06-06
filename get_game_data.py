import os
import sys
from subprocess import PIPE, run
import json
import shutil

def main(source,target):
    pass


if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) != 3:
        raise ValueError("you need to pass a source and a target directory - only")
    
source, target = args[1:]
main(source, target)