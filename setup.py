#!/usr/bin/env python3

import sys

try:
    from setuptools import setup, Extension
except ImportError:
    print("It looks like you don't have setuptools installed.",
          "I will not fall back using distutils.",
          sep='\n', file=sys.stderr)
    sys.exit(1)


CFLAGS = ["-std=c++11", "-Wall", "-I/usr/include/eigen3/"]


def get_ext_modules():
    """
    Return a list of Extension instances for the setup() call.
    """
    # Note we don't import Numpy at the toplevel, since setup.py
    # should be able to run without Numpy for pip to discover the
    # build dependencies
    import numpy.distutils.misc_util as np_misc

    # Inject required options for extensions compiled against the Numpy
    # C API (include dirs, library dirs etc.)
    np_compile_args = np_misc.get_info('npymath')

    ext_mongeampere = Extension(
        name="SemidiscreteOT.mongeampere",
        sources=["SemidiscreteOT/MongeAmpere.cpp"],
        extra_compile_args=CFLAGS,
        **np_compile_args)

    ext_modules = [ext_mongeampere]

    return ext_modules


metadata = dict(
    name='SemidiscreteOT',
    description="Compute semidiscrete optimal transport",
    version="0.1",

    author="Continuum Analytics, Inc.",
    author_email="numba-users@continuum.io",
    url="http://github.com/FedericoStra/SemidiscreteOT",

    packages=['SemidiscreteOT'],
    ext_modules=get_ext_modules(),

    setup_requires=['numpy'],
    install_requires=['numpy'],

    license="GPL",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Compilers",
        ],
    )

setup(**metadata)
