from setuptools import setup # type: ignore
from Cython.Build import cythonize # type: ignore
from setuptools.extension import Extension # type: ignore

extensions = cythonize([
    Extension("logprocessor.libs.fast_metric_merge", ["logprocessor/libs/fast_metric_merge.pyx"])
])

setup(
    name = "Logprocessor",
    ext_modules = extensions,
)