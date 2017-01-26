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
    # Add other required libraries
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

    setup_requires=['numpy'],
    install_requires=['numpy', 'scipy', 'matplotlib'],

    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Mathematics",
        ],
    )

with open("README.md") as f:
    metadata['long_description'] = f.read()

if __name__ == '__main__':
    setup(**metadata)
