DESCRIPTION = "Plan Too observation with ZTF"
LONG_DESCRIPTION = """Plan Too observation with ZTF"""

DISTNAME = "modelSED"
AUTHOR = "Simeon Reusch"
MAINTAINER = "Simeon Reusch"
MAINTAINER_EMAIL = "simeon.reusch@desy.de"
URL = "https://github.com/simeonreusch/ztf_plan_too/"
LICENSE = "BSD (3-clause)"
DOWNLOAD_URL = "https://github.com/simeonreusch/ztf_plan_too/archive/v0.1-alpha.tar.gz"
VERSION = "v0.1-alpha"

try:
    from setuptools import setup, find_packages

    _has_setuptools = True
except ImportError:
    from distutils.core import setup

    _has_setuptools = False


def check_dependencies():
    install_requires = []

    # Make sure dependencies exist. This is ongoing
    try:
        import astropy
    except ImportError:
        install_requires.append("astropy")
    try:
        import numpy
    except ImportError:
        install_requires.append("numpy")
    try:
        import astroplan
    except ImportError:
        install_requires.append("astroplan")
    try:
        import pandas
    except ImportError:
        install_requires.append("pandas")
    try:
        import matplotlib
    except ImportError:
        install_requires.append("matplotlib")
    try:
        import bs4
    except ImportError:
        install_requires.append("bs4")
    try:
        import ztfquery
    except ImportError:
        install_requires.append("ztfquery")
    try:
        import requests
    except ImportError:
        install_requires.append("requests")

    return install_requires


if __name__ == "__main__":

    install_requires = check_dependencies()

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ["modelSED"]

    setup(
        name=DISTNAME,
        author=AUTHOR,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=packages,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: BSD License",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ],
    )
