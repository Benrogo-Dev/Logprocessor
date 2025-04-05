# type: ignore
from setuptools import setup , find_packages
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
sources = glob("logprocessor/libs/*.%s" % (filename_ext,))
extensions = [
    Extension(source.split(".")[0].replace(os.path.sep, "."),
              sources=[source]
    )
for source in sources]
cmdclass = {"build_ext": build_ext} if USING_CYTHON else {}

setup(
    ext_modules=extensions,
    cmdclass=cmdclass,
    packages = find_packages() + ["logprocessor.libs"],
    test_suite="tests"
)