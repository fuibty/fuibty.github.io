from distutils.core import setup
from Cython.Build import cythonize

setup(name='find n4',
      ext_modules=cythonize("findN4.pyx"))
