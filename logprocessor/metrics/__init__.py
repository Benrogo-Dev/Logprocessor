from os.path import dirname, basename, isfile, join
import glob
import importlib

modules = glob.glob(join(dirname(__file__), "*.py"))

__all__ = [
    basename(f)[:-3] for f in modules
    if (isfile(f)
        and not basename(f).startswith("_")
        )
]

for metric_name in __all__:
    globals()[metric_name] = importlib.import_module(
        f".{metric_name}", __package__
    )
