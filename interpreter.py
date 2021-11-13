import subprocess
from parser  import *
from visitor import *

def printArgs(args):
    print(*args)

def runCommand(args):
    subprocess.run(args)

# Commands hash

COMMANDS = {
    "print": printArgs,
    "cmd": runCommand
}

################

class Interpreter:
    def __init__(self):
        self.stack = [[]]

    def interpret(self, ast):
        visitor = NodeVisitor(self)
        for paper in ast.papers:
            paper.accept(visitor)

    def new_frame(self):
        self.stack.append([])

    def pop_frame(self):
        self.stack.pop()

    def define_variable(self, var_id, var_value):
        frame = self.stack[-1]
        for i in range(len(frame)):
            if var_id == frame[i][0]:
                frame[i][1] = var_value
                return
        frame.append([var_id, var_value])

    def get_variable(self, var_id):
        for frame in self.stack[::-1]:
            for i in range(len(frame)):
                if var_id == frame[i][0]:
                    return frame[i][1]
        raise Exception(f"Undefined variable {var_id}.")
            
    def runStandardFn(self, fn_name, args):
        if not fn_name in COMMANDS.keys():
            raise Exception(f"Unknown function {fn_name}.")
        return COMMANDS[fn_name](args)
