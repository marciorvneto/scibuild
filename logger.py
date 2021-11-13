import time

def timestamp():
    current_time = time.gmtime()
    formatted = time.strftime('%Y-%m-%d %H:%M:%S', current_time)
    return formatted

class Logger:
    def __init__(self, name: str):
        self.name = name

    def log(self,text: str):
        print(f"\x1b[39m[{self.name}] [{timestamp()}] {text}\x1b[0m")

    def info(self,text: str):
        print(f"\x1b[34m[{self.name}] [{timestamp()}] {text}\x1b[0m")

    def success(self,text: str):
        print(f"\x1b[32m[{self.name}] [{timestamp()}] {text}\x1b[0m")

    def warn(self,text: str):
        print(f"\x1b[33m[{self.name}] [{timestamp()}] {text}\x1b[0m")

    def error(self,text: str):
        print(f"\x1b[31m[{self.name}] [{timestamp()}] {text}\x1b[0m")

scibuild_logger= Logger("Scibuild")
