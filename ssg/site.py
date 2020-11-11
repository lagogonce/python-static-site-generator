from os import mkdir
from pathlib import *

class Site:
    """Site class"""

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest + "/" + path.relative_to()
        mkdir(directory,parents=True,exists_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exists_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                mkdir(path)






