import dolfinx
from importlib.metadata import metadata

meta = metadata("package")
__version__ = meta["Version"]
__author__ = meta["Author-email"]
__license__ = meta["License"]
__email__ = meta["Author-email"]
__program_name__ = meta["Name"]


def compute():
    print("Computing...")
    print("Dolfinx version:", dolfinx.__version__)
    return 0
