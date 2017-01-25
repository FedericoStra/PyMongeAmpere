import sys
from setuptools import setup, Extension


CFLAGS = ["-std=c++11", "-Wall"]


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
    compile_args = np_misc.get_info('npymath')

    compile_args['include_dirs'] += ["/usr/include/eigen3/"]
    compile_args['libraries'] += ["boost_numpy", "gmp",
        "CGAL", "CGAL_Core", "CGAL_ImageIO"]

    ext_mongeampere = Extension(
        name="SemidiscreteOT.MongeAmpere",
        sources=["SemidiscreteOT/MongeAmpere.cpp"],
        extra_compile_args=CFLAGS,
        **compile_args)

    ext_modules = [ext_mongeampere]

    return ext_modules


metadata = dict(
    name='SemidiscreteOT',
    description="Compute semidiscrete optimal transport",
    version="0.1",

    author="Federico Stra",
    author_email="federico.stra@sns.it",
    url="http://github.com/FedericoStra/SemidiscreteOT",

    packages=['SemidiscreteOT'],
    ext_modules=get_ext_modules(),

    setup_requires=[],
    install_requires=['numpy'],

    license="GPL",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        ],
    )

setup(**metadata)
