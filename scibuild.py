#!/usr/bin/python3

import os
import sys
from tokenizer import *
from parser import *
from interpreter import *
from logger import scibuild_logger 

args = sys.argv[1:]

if len(sys.argv) == 1:
    print("USAGE: scibuild <filepath>")
    quit()

file_path = os.path.abspath(args[0])

try:
    with open(file_path, "r") as file:
        t = Tokenizer(file.read())
        p = Parser()
        ast  = p.parse(t)
        i = Interpreter()
        try:
            i.interpret(ast)
        except Exception as e:
            scibuild_logger.error(f"Error reading file: {e}") 
            quit(1)
except Exception as e:
    scibuild_logger.error(f"File \"{file_path}\" not found.")
    quit(1)


