from os.path import dirname, basename, isfile, join
import glob
import importlib

modules = glob.glob(join(dirname(__file__), "*.py"))
registered_module = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

for lib in registered_module:
    globals()[lib] = importlib.import_module("task." + lib)