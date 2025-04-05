# type: ignore
from setuptools import setup 
from glob import glob
import os

try:
    from Cython.Distutils.extension import Extension
    from Cython.Distutils import build_ext
except ImportError:
    from setuptools import Extension
    USING_CYTHON = False
else:
    USING_CYTHON = True

filename_ext = "pyx" if USING_CYTHON else "c"
sources = glob("libs/*.%s" % (filename_ext,))
extensions = [
    Extension(source.split(".")[0].replace(os.path.sep, "."),
              sources=[source]
    )
for source in sources]
cmdclass = {"build_ext": build_ext} if USING_CYTHON else {}

setup(
    name="logprocessor",
    version="1.0.0",
    author="Ben_Da_Builder",
    author_email="ben@benrogo.net",
    description="A modular, python-based log metrics processor.",
    ext_modules=extensions,
    cmdclass=cmdclass,
    packages = ["logprocessor"],
    test_suite="tests"
)